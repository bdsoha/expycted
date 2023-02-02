from __future__ import annotations

from expycted import expect
from expycted.matchers import IsMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(1)

    assert isinstance(expectation.to.be, IsMatcher)

    expectation.to.be(1)

    with context.raises:
        expectation.to_not.be(1)


@parametrize_expectation(
    [
        (1, 1),
        ("1", "1"),
        (stubs.LIST, stubs.LIST),
        (stubs.SINGLETON_OBJECT, stubs.SINGLETON_OBJECT),
    ],
    matcher=IsMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        ([1, "hello", "world"], [1, "hello", "world"]),
        (stubs.NOT_SINGLETON_OBJECT(), stubs.NOT_SINGLETON_OBJECT()),
    ],
    matcher=IsMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
