from expycted import expect
from expycted.matchers import EqualMatcher

from helpers.stubs import EQUAL, NOT_EQUAL
from helpers.utils import expected_actual_params


def test_via_expect(context):
    expectation = expect(True)

    assert isinstance(expectation.to.equal, EqualMatcher)
    assert isinstance(expectation.to.be_equal_to, EqualMatcher)

    expectation.to_not.equal(False)

    with context.raises:
        expectation.to.equal(False)


@expected_actual_params(EQUAL)
def test_matches(expected, actual):
    matcher = EqualMatcher(expected)

    assert matcher(actual) is True


@expected_actual_params(NOT_EQUAL)
def test_not_matches(expected, actual):
    matcher = EqualMatcher(expected)

    assert matcher(actual) is False
