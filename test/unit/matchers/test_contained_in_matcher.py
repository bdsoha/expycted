from __future__ import annotations

from expycted import expect
from expycted.matchers import ContainedInMatcher

from helpers import stubs
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
        (2, [2], "list"),
        ("a", {"a", "b"}, "set"),
        ("bc", "abcd", "substr"),
        ("", "abcd", "empty str"),
        ("a", {"a": 1, "b": 2}, "dict"),
        ("string", "string", "full str"),
    ],
    matcher=ContainedInMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        (2, [1], "list"),
        (["a"], ["a", 2], "item in list"),
        ("ings", "string", "str"),
        ("c", {"a": 1, "b": 2}, "dict"),
    ],
    matcher=ContainedInMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False


@parametrize_expectation(
    [
        ("hello2", 2, "int in str"),
        stubs.TRUE_STR_EQUIVALENT,
        (stubs.NOT_SINGLETON_OBJECT(), stubs.NOT_SINGLETON_OBJECT()),
        (
            stubs.SINGLETON_OBJECT(),
            stubs.SINGLETON_OBJECT(),
        ),
    ],
    matcher=ContainedInMatcher,
    wrap=False,
)
def test_type_error(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
