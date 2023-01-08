from __future__ import annotations

from expycted import expect
from expycted.matchers import NumericMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(1)

    assert isinstance(expectation.to.be_numeric, NumericMatcher)
    assert isinstance(expectation.to.be_a_number, NumericMatcher)

    expectation.to.be_numeric()

    with context.raises:
        expectation.to_not.be_numeric()


@parametrize_expectation(
    [
        1,
        "1",
        3,
        3.2,
        "3.2",
        1e1,
        "1e1",
        1_001_123,
        "1_001_123",
    ],
    matcher=NumericMatcher,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher() is True


@parametrize_expectation(
    [
        True,
        False,
        "a",
        [1, 2],
        set(),
        tuple(),
        lambda x: x,
        stubs.PERSON,
    ],
    matcher=NumericMatcher,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
