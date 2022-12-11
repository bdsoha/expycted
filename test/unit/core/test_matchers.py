from traceback import StackSummary
from unittest.mock import Mock
from expycted.core.matchers import BaseMatcher
from expycted.core.messages import Message
from expycted.core.utilities import SENTINEL
from expycted.core.exceptions import MatcherError

import pytest


class AlwaysTrueMatcher(BaseMatcher):
    def __init__(self, actual, *, negated: bool = False):
        super().__init__(actual, negated=negated)
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

    matcher.mock.assert_called_once_with(SENTINEL)

def test_negated():
    matcher = AlwaysTrueMatcher(True, negated=True)

    assert matcher() is False
    matcher.mock.assert_called_once_with(SENTINEL)

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
    allowed = AllowedTypesMatcher(True)

    assert matcher.name() == "always_true"
    assert allowed.name() == "allowed_types"

def test_message(matcher):
    assert isinstance(matcher.message(), Message)