from expycted import expect
from expycted.matchers.values import EqualMatcher, BeEmptyMatcher
from expycted.core.exceptions import MatcherError


from helpers.utils import expected_actual_params, expected_params
from helpers import stubs

import pytest

class TestEqualMatcher:
    def test_via_expect(self, context):
        expectation = expect(True)

        assert isinstance(expectation.to.equal, EqualMatcher)
        assert isinstance(expectation.to.be_equal_to, EqualMatcher)

        expectation.to_not.equal(False)

        with context.raises:
            expectation.to.equal(False)

    @expected_actual_params(stubs.EQUAL)
    def test_matches(self, expected, actual):
        matcher = EqualMatcher.safe(expected)

        assert matcher(actual) is True

    @expected_actual_params(stubs.NOT_EQUAL)
    def test_not_matches(self, expected, actual):
        matcher = EqualMatcher.safe(expected)

        assert matcher(actual) is False


class TestBeEmptyMatcher:
    def test_via_expect(self, context):
        expectation = expect([])

        assert isinstance(expectation.to.be_empty, BeEmptyMatcher)

        expectation.to.be_empty()

        with context.raises:
            expectation.to_not.be_empty()

    @expected_params((*stubs.EMPTY, *stubs.EMPTY_GENERATORS()), extract_ids=False)
    def test_matches(self, expected):
        matcher = BeEmptyMatcher.safe(expected)

        assert matcher() is True

    @expected_params(stubs.NOT_EMPTY, extract_ids=False)
    def test_not_matches(self, expected):
        matcher = BeEmptyMatcher.safe(expected)

        assert matcher() is False

    @expected_params(stubs.NOT_EMPTY_TYPE_ERROR, extract_ids=False)
    def test_type_error(self, expected):
        matcher = BeEmptyMatcher.safe(expected)

        with pytest.raises(MatcherError):
            matcher()
