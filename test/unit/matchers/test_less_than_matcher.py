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


# @parametrize_expectation(
#     [
#         (stubs.SINGLETON_OBJECT(), stubs.SINGLETON_OBJECT()),
#         (True, 1, "True int equivalent"),
#         (False, 0, "False int equivalent"),
#         (1, 1.0, "int float equivalent"),
#         (True, True, "bool"),
#         (1, 1, "int"),
#         (1.1, 1.1, "float"),
#         ("hello", "hello", "str"),
#         ([True, 1.1], [True, 1.1], "list"),
#         ({True, 1.1}, {1.1, True}, "set ignore order"),
#         ({"a": [True, 1.1]}, {"a": [True, 1.1]}, "dict"),
#     ],
#     matcher=EqualMatcher,
#     wrap=False,
# )
# def test_matches(expectation):
#     matcher = expectation.matcher()

#     assert matcher(expectation.expected) is True


# @parametrize_expectation(
#     [
#         (stubs.NOT_SINGLETON_OBJECT(), stubs.NOT_SINGLETON_OBJECT()),
#         (True, "True", "bool (True) str equivalent"),
#         (False, "False", "bool (False) str equivalent"),
#         (1, "1", "int str equivalent"),
#         ([True, 1.1], (True, 1.1), "list tuple equivalent"),
#         (False, None, "False None equivalent"),
#         (b"hello", "hello", "byte-str str equivalent"),
#     ],
#     matcher=EqualMatcher,
#     wrap=False,
# )
# def test_not_matches(expectation):
#     matcher = expectation.matcher()

#     assert matcher(expectation.expected) is False
