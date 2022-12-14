from __future__ import annotations

from expycted import expect
from expycted.matchers import IsFalseMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(False)

    assert isinstance(expectation.to.be_false, IsFalseMatcher)

    assert isinstance(expectation.to.be_falsy, IsFalseMatcher)
    assert isinstance(expectation.to.be_falsey, IsFalseMatcher)
    assert isinstance(expectation.to.be_falsish, IsFalseMatcher)

    expectation.to.be_false()

    with context.raises:
        expectation.to_not.be_false()


def test_matches():
    matcher = IsFalseMatcher(False)

    assert matcher() is True
    assert matcher.weak() is True
    assert matcher.from_str() is True


@parametrize_expectation(
    [
        0,
        "0",
        "false",
        "False",
        "FALSE",
    ],
    matcher=IsFalseMatcher,
)
def test_not_matches_and_weak(expectation):
    matcher = expectation.matcher()

    assert matcher() is False
    assert matcher.from_str() is True


@parametrize_expectation(
    [
        False,
        stubs.ZERO(),
        stubs.EMPTY_STRING(),
        stubs.EMPTY_LIST(),
        stubs.EMPTY_RANGE(),
    ],
    matcher=IsFalseMatcher,
)
def test_be_falsey_matches(expectation):
    matcher = expectation.matcher()

    assert matcher.weak() is True


@parametrize_expectation(
    [
        True,
        "0",
        stubs.INT(),
        stubs.STRING(),
        stubs.LIST(),
        stubs.RANGE(),
        stubs.SINGLETON_OBJECT(),
    ],
    matcher=IsFalseMatcher,
)
def test_be_falsey_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher.weak() is False
