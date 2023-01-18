from __future__ import annotations

from expycted import expect
from expycted.matchers import IsMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


@parametrize_expectation(
    [
        (stubs.EMPTY_LIST, stubs.EMPTY_LIST),
        (stubs.EMPTY_SET, stubs.EMPTY_SET),
        (stubs.EMPTY_STRING, stubs.EMPTY_STRING),
        (stubs.EMPTY_BSTRING, stubs.EMPTY_BSTRING),
        (stubs.EMPTY_TUPLE, stubs.EMPTY_TUPLE),
        (stubs.EMPTY_DICT, stubs.EMPTY_DICT),
        (stubs.EMPTY_RANGE, stubs.EMPTY_RANGE),
        (stubs.EMPTY_GENERATOR, stubs.EMPTY_GENERATOR),
        (stubs.INT, stubs.INT),
        (stubs.ZERO, stubs.ZERO),
        (stubs.INT_STR, stubs.INT_STR),
        (stubs.FLOAT, stubs.FLOAT),
        (stubs.FLOAT_STR, stubs.FLOAT_STR),
        (stubs.FUNCTION_BUILT, stubs.FUNCTION_BUILT),
        (stubs.LIST, stubs.LIST),
        (stubs.SET, stubs.SET),
        (stubs.STRING, stubs.STRING),
        (stubs.BSTRING, stubs.BSTRING),
        (stubs.TUPLE, stubs.TUPLE),
        (stubs.DICT, stubs.DICT),
        (stubs.RANGE, stubs.RANGE),
        (stubs.GENERATOR, stubs.GENERATOR),
        (stubs.SINGLETON_OBJECT, stubs.SINGLETON_OBJECT),
        (stubs.NOT_SINGLETON_OBJECT, stubs.NOT_SINGLETON_OBJECT),
    ],
    matcher=IsMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher(to_match=expectation.expected)

    assert matcher() is True


@parametrize_expectation(
    [
        (stubs.EMPTY_LIST, stubs.DescribedParam([], description="Empty list")),
        (stubs.EMPTY_SET, stubs.DescribedParam(set(), description="Empty set")),
        (stubs.EMPTY_DICT, stubs.DescribedParam({}, description="Empty dict")),
        (
            stubs.EMPTY_RANGE,
            lambda: stubs.DescribedParam(range(0), description="Empty range"),
        ),
        (
            stubs.EMPTY_GENERATOR,
            lambda: stubs.DescribedParam(
                (i for i in range(0)),
                description="Empty generator",
            ),
        ),
        (stubs.FLOAT, stubs.DescribedParam(1.1, description="Example float")),
        (
            stubs.FLOAT_STR,
            stubs.DescribedParam("1.1", description="Float value as string"),
        ),
        (
            stubs.LIST,
            stubs.DescribedParam([1, "hello", "world"], description="Example list"),
        ),
        (
            stubs.SET,
            stubs.DescribedParam({1, "hello", "world"}, description="Example set"),
        ),
        (
            stubs.STRING,
            stubs.DescribedParam("hello world", description="Example string"),
        ),
        (
            stubs.BSTRING,
            stubs.DescribedParam(b"hello world", description="Example byte string"),
        ),
        (
            stubs.TUPLE,
            stubs.DescribedParam((1, "hello", "world"), description="Example tuple"),
        ),
        (
            stubs.DICT,
            stubs.DescribedParam({1: "hello world"}, description="Example dict"),
        ),
        (
            stubs.RANGE,
            lambda: stubs.DescribedParam(range(1), description="Example range"),
        ),
        (
            stubs.GENERATOR,
            lambda: stubs.DescribedParam(
                (i for i in range(1)), description="Example generator"
            ),
        ),
        (
            stubs.SINGLETON_OBJECT,
            stubs.DescribedParam(stubs.Person(), description="Singleton object"),
        ),
        (
            stubs.NOT_SINGLETON_OBJECT,
            lambda: stubs.DescribedParam(
                stubs.Person(),
                description="Not singleton object",
            ),
        ),
    ],
    matcher=IsMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher(to_match=expectation.expected)

    assert matcher() is False
