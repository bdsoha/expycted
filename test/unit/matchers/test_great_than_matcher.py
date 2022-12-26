from __future__ import annotations

from expycted import expect
from expycted.matchers import GreatThanMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(2)

    assert isinstance(expectation.to.be_great, GreatThanMatcher)
    assert isinstance(expectation.to.be_great_than, GreatThanMatcher)
    assert isinstance(expectation.to.be_greater, GreatThanMatcher)
    assert isinstance(expectation.to.be_greater_than, GreatThanMatcher)

    assert isinstance(expectation.to.be_great_or_equal, GreatThanMatcher)
    assert isinstance(expectation.to.be_great_than_or_equal_to, GreatThanMatcher)
    assert isinstance(expectation.to.be_greater_or_equal_to, GreatThanMatcher)
    assert isinstance(expectation.to.be_greater_than_or_equal_to, GreatThanMatcher)

    expectation.to.be_great_than(1)
    expectation.to.be_great_than_or_equal_to(2)

    with context.raises:
        expectation.to.be_great_than(2)


@parametrize_expectation(
    [
        ("hello world", "hello"),
        (3, 2),
        (3.2, 3),
        ([2], [1]),
        ([1, 0], [1]),
    ],
    matcher=GreatThanMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ("hello world", "hello"),
        ("hello", "hello"),
        (3, 2),
        (2, 2),
        (3.2, 3),
        ([2], [1]),
        ([1], [1]),
    ],
    matcher=GreatThanMatcher,
    wrap=False,
)
def test_or_equal_matches(expectation):
    matcher = expectation.matcher(or_equal=True)

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ("hello", "hello world"),
        (2, 3),
        (3, 3.2),
        ([1], [2]),
        ([1], [1, 0]),
    ],
    matcher=GreatThanMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
