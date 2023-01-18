from __future__ import annotations

from expycted import expect
from expycted.matchers import InheritMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(1)

    assert isinstance(expectation.to.inherit, InheritMatcher)
    assert isinstance(expectation.to.have_parent, InheritMatcher)
    assert isinstance(expectation.to.be_subclass_of, InheritMatcher)

    expectation.to.inherit(int)

    with context.raises:
        expectation.to.inherit(str)


@parametrize_expectation(
    [
        ([1], list),
        ({"a", "b"}, set),
        ({"a": 1, "b": 2}, dict),
        (2, int),
        (1.0, float),
        ("a", str),
        (True, bool),
        (1, object),
        (stubs.PERSON, stubs.Person),
        (type(stubs.PERSON), type),
        (stubs.PERSON, stubs.Parent),
        (stubs.PERSON, object),
    ],
    matcher=InheritMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [("string", "str")],
    matcher=InheritMatcher,
    wrap=False,
)
def test_to_inherit_type_error(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False


@parametrize_expectation(
    [("string", int), (1, str), (1, float), (1.0, int)],
    matcher=InheritMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
