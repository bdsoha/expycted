from __future__ import annotations

from expycted import expect
from expycted.matchers import LessThanMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(1)

    assert isinstance(expectation.to.be_less, LessThanMatcher)
    assert isinstance(expectation.to.be_less_than, LessThanMatcher)
    assert isinstance(expectation.to.be_lesser, LessThanMatcher)
    assert isinstance(expectation.to.be_lesser_than, LessThanMatcher)

    assert isinstance(expectation.to.be_less_or_equal, LessThanMatcher)
    assert isinstance(expectation.to.be_less_than_or_equal_to, LessThanMatcher)
    assert isinstance(expectation.to.be_lesser_or_equal_to, LessThanMatcher)
    assert isinstance(expectation.to.be_lesser_than_or_equal_to, LessThanMatcher)

    expectation.to.be_less_than(2)
    expectation.to.be_less_than_or_equal_to(1)

    with context.raises:
        expectation.to.be_less_than(1)


@parametrize_expectation(
    [
        ("hello", "hello world"),
        (2, 3),
        (3, 3.2),
        ([1], [2]),
        ([1], [1, 0]),
    ],
    matcher=LessThanMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ("hello", "hello world"),
        ("hello", "hello"),
        (2, 3),
        (2, 2),
        (3, 3.2),
        ([1], [2]),
        ([1], [1]),
    ],
    matcher=LessThanMatcher,
    wrap=False,
)
def test_or_equal_matches(expectation):
    matcher = expectation.matcher(or_equal=True)

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ("hello world", "hello"),
        (3, 2),
        (3.2, 3),
        ([2], [1]),
        ([1, 0], [1]),
    ],
    matcher=LessThanMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
