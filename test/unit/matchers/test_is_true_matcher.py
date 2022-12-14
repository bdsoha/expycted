from expycted import expect
from expycted.matchers import IsTrueMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(True)

    assert isinstance(expectation.to.be_true, IsTrueMatcher)

    assert isinstance(expectation.to.be_truthy, IsTrueMatcher)
    assert isinstance(expectation.to.be_truey, IsTrueMatcher)
    assert isinstance(expectation.to.be_trueish, IsTrueMatcher)

    expectation.to.be_true()

    with context.raises:
        expectation.to_not.be_true()


def test_matches():
    matcher = IsTrueMatcher(True)

    assert matcher() is True
    assert matcher.weak() is True
    assert matcher.from_str() is True


@parametrize_expectation(
    [
        1,
        "1",
        "true",
        "True",
        "TRUE",
    ],
    matcher=IsTrueMatcher,
)
def test_not_matches_and_weak(expectation):
    matcher = expectation.matcher()

    assert matcher() is False
    assert matcher.from_str() is True


@parametrize_expectation(
    [
        "False",
        stubs.LIST(),
        stubs.GENERATOR(),
        stubs.RANGE(),
        stubs.INT(),
        stubs.SINGLETON_OBJECT(),
    ],
    matcher=IsTrueMatcher,
)
def test_be_truthy_matches(expectation):
    matcher = expectation.matcher()

    assert matcher.weak() is True


@parametrize_expectation(
    [
        False,
        stubs.EMPTY_STRING(),
        stubs.EMPTY_LIST(),
        stubs.EMPTY_RANGE(),
        stubs.ZERO(),
    ],
    matcher=IsTrueMatcher,
)
def test_be_truthy_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher.weak() is False
