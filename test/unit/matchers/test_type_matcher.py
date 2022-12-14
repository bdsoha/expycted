from expycted import expect
from expycted.matchers import TypeMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect(5.5)

    assert isinstance(expectation.to.be_of_type, TypeMatcher)
    assert isinstance(expectation.to.be_type, TypeMatcher)
    assert isinstance(expectation.to.have_type, TypeMatcher)

    expectation.to.be_of_type(float)

    with context.raises:
        expectation.to.be_of_type(int)


@parametrize_expectation(
    [
    ([1], list),
    (2, int),
    ("a", str),
    ({"a", "b"}, set),
    ({"a": 1, "b": 2}, dict),
    (True, bool),
    (stubs.SINGLETON_OBJECT(), stubs.Person),
    (1, int),
    (1.0, float),
    (type(stubs.SINGLETON_OBJECT()), type),
    ],
    matcher=TypeMatcher,
    wrap=False,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is True


@parametrize_expectation(
    [
        (stubs.SINGLETON_OBJECT(), stubs.Parent),
        (stubs.SINGLETON_OBJECT(), object),
        (stubs.BSTRING(), str),
        (1, float),
        (1.0, int),
    ],
    matcher=TypeMatcher,
    wrap=False,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher(expectation.expected) is False
