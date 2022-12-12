import pytest

from expycted import expect
from expycted.core.exceptions import MatcherError
from expycted.matchers import BeEmptyMatcher
from helpers.stubs import (
    EMPTY,
    EMPTY_GENERATORS,
    NOT_EMPTY,
    NOT_EMPTY_TYPE_ERROR
)
from helpers.utils import expected_params


def test_via_expect(context):
    expectation = expect([])

    assert isinstance(expectation.to.be_empty, BeEmptyMatcher)

    expectation.to.be_empty()

    with context.raises:
        expectation.to_not.be_empty()

@expected_params((*EMPTY, *EMPTY_GENERATORS()), extract_ids=False)
def test_matches(expected):
    matcher = BeEmptyMatcher(expected)

    assert matcher() is True

@expected_params(NOT_EMPTY, extract_ids=False)
def test_not_matches(expected):
    matcher = BeEmptyMatcher(expected)

    assert matcher() is False

@expected_params(NOT_EMPTY_TYPE_ERROR, extract_ids=False)
def test_type_error(expected):
    matcher = BeEmptyMatcher(expected)

    with pytest.raises(MatcherError):
        matcher()
