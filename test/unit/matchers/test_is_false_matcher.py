from __future__ import annotations

import pytest

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
    strict = IsFalseMatcher(False)
    loose = IsFalseMatcher(False, strict=False)

    assert strict() is True
    assert loose() is True


@pytest.mark.skip(reason="Implement when allowing multiple qualifiers")
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
    from_str = expectation.matcher(from_str=True)

    assert matcher() is False
    assert from_str() is True


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
    matcher = expectation.matcher(strict=False)

    assert matcher() is True


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
    matcher = expectation.matcher(strict=False)

    assert matcher() is False
