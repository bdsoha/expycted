from __future__ import annotations

from expycted import expect
from expycted.matchers import ContainMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect([1])

    assert isinstance(expectation.to.contain, ContainMatcher)
    assert isinstance(expectation.to.has, ContainMatcher)
    assert isinstance(expectation.to.have, ContainMatcher)
    assert isinstance(expectation.to.include, ContainMatcher)

    expectation.to.contain(1)

    with context.raises:
        expectation.to_not.contain(1)


@parametrize_expectation(
    [
        ([2], 2, "list"),
        ({"a", "b"}, "a", "set"),
        ("abcd", "bc", "substr"),
        ("abcd", "", "empty str"),
        ({"a": 1, "b": 2}, "a", "dict"),
        ("string", "string", "full str"),
    ],
    matcher=ContainMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ([1], 2, "list"),
        (["a", 2], ["a"], "item in list"),
        ("string", "ings", "str"),
        ({"a": 1, "b": 2}, "c", "dict"),
    ],
    matcher=ContainMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False


@parametrize_expectation(
    [
        ("hello2", 2, "int in str"),
        stubs.TRUE_STR_EQUIVALENT,
        stubs.COPY_OBJECT,
        stubs.SAME_OBJECT,
    ],
    matcher=ContainMatcher,
    wrap=False,
)
def test_type_error(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
