from __future__ import annotations

from expycted import expect
from expycted.matchers import ContainedInMatcher

from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(1)

    assert isinstance(expectation.to.be_contained_in, ContainedInMatcher)
    assert isinstance(expectation.to.be_in, ContainedInMatcher)
    assert isinstance(expectation.to.be_included_in, ContainedInMatcher)

    expectation.to.be_contained_in([1])

    with context.raises:
        expectation.to_not.be_contained_in([1])


@parametrize_expectation(
    [
        (2, [2]),
        ("a", {"a", "b"}),
        ("bc", "abcd"),
        ("", "abcd"),
        ("a", {"a": 1, "b": 2}),
        ("string", "string"),
    ],
    matcher=ContainedInMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        (2, [1]),
        (["a"], ["a", 2]),
        ("ings", "string"),
        ("c", {"a": 1, "b": 2}),
    ],
    matcher=ContainedInMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
