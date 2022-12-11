from expycted import expect
from expycted.matchers.values import EqualMatcher

from helpers.utils import expected_actual_params
from helpers import stubs


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