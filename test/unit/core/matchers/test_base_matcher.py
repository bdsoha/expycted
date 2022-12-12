from unittest.mock import Mock

import pytest

from expycted.core.exceptions import MatcherError
from expycted.core.matchers import BaseMatcher
from expycted.core.messages import Message


class AlwaysTrueMatcher(BaseMatcher):
    def __init__(self, actual, **kwargs):
        super().__init__(actual, **kwargs)
        self.mock = Mock()
        self.mock.return_value = True

    def _matches(self, *, expected, **kwargs) -> bool:
        return self.mock(expected, **kwargs)


class AllowedTypesMatcher(AlwaysTrueMatcher):
    ALLOWED_TYPES = (list, str)


@pytest.fixture
def matcher():
    return AlwaysTrueMatcher(True)


def test_matches(matcher):
    assert matcher() is True

    matcher.mock.assert_called_once_with(...)


def test_negated():
    matcher = AlwaysTrueMatcher(True, negated=True)

    assert matcher() is False
    matcher.mock.assert_called_once_with(...)


def test_with_expected(matcher):
    assert matcher("any expected value") is True

    matcher.mock.assert_called_once_with("any expected value")


@pytest.mark.parametrize("actual", [(1, 2), b"hello"])
def test_allowed_types(actual):
    matcher = AllowedTypesMatcher(actual)

    with pytest.raises(MatcherError):
        matcher()

    matcher.mock.assert_not_called()


def test_name(matcher):
    assert matcher.name() == "always_true"
    assert AllowedTypesMatcher(True).name() == "allowed_types"
    assert AllowedTypesMatcher(True, alias="other").name() == "other"


def test_message(matcher):
    assert isinstance(matcher.message(), Message)
