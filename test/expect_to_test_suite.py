import pytest
from expycted import expect

from test_utils import DOES_NOT_RAISE, RAISES_ASSERTION, expected_params, expected_actual_params


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


singleton = None


@pytest.fixture
def get_singleton():
    global singleton
    if singleton is None:
        singleton = Person("John", 30)
    return singleton


@expected_actual_params([
    (1, 2, RAISES_ASSERTION),
    (1, 1, DOES_NOT_RAISE),
    (1, 0, RAISES_ASSERTION),
    (0, 0, DOES_NOT_RAISE),
    (True, "True", RAISES_ASSERTION),
    (True, True, DOES_NOT_RAISE),
    (True, False, RAISES_ASSERTION),
    ("string", "another", RAISES_ASSERTION),
    ("string", "string", DOES_NOT_RAISE),
    (1, "1", RAISES_ASSERTION),
    (get_singleton, get_singleton, DOES_NOT_RAISE),
    (get_singleton, Person("John", 30), RAISES_ASSERTION),
])
def test_to_equal(expected, actual, context):
    with context:
        expect(expected).to.equal(actual)

    with context:
        expect(expected).to.be_equal_to(actual)


@expected_actual_params([
    (1, 2, RAISES_ASSERTION),
    (1, 1, DOES_NOT_RAISE),
    (1, 0, RAISES_ASSERTION),
    (0, 0, DOES_NOT_RAISE),
    (True, "True", DOES_NOT_RAISE),
    (True, True, DOES_NOT_RAISE),
    (True, False, RAISES_ASSERTION),
    ("string", "another", RAISES_ASSERTION),
    ("string", "string", DOES_NOT_RAISE),
    (1, "1", DOES_NOT_RAISE),
    (get_singleton, get_singleton, DOES_NOT_RAISE),
    (get_singleton, Person("John", 30), RAISES_ASSERTION),
    (1, 1.0, DOES_NOT_RAISE),
    (2.0, 3, RAISES_ASSERTION),
])
def test_to_be(expected, actual, context):
    with context:
        expect(expected).to.be(actual)


@expected_actual_params([
    ([1], None, RAISES_ASSERTION),
    ([2], 2, DOES_NOT_RAISE),
    (["a", 2], ["b"], RAISES_ASSERTION),
    ({"a", "b"}, "a", DOES_NOT_RAISE),
    ("abcd", "bc", DOES_NOT_RAISE),
    ({"a": 1, "b": 2}.values(), 2, DOES_NOT_RAISE),
    ("True", True, RAISES_ASSERTION),
    ("string", "ings", RAISES_ASSERTION),
    ("string", "string", DOES_NOT_RAISE),
    (get_singleton, get_singleton, RAISES_ASSERTION),
    (get_singleton, Person("John", 30), RAISES_ASSERTION),
])
def test_to_contain(expected, actual, context):
    with context:
        expect(expected).to.contain(actual)

    with context:
        expect(expected).to.have(actual)

    with context:
        expect(expected).to.include(actual)


@expected_actual_params([
    (None, [1], RAISES_ASSERTION),
    (2, [2], DOES_NOT_RAISE),
    (["b"], ["a", 2], RAISES_ASSERTION),
    ("a", {"a", "b"}, DOES_NOT_RAISE),
    ("bc", "abcd", DOES_NOT_RAISE),
    (2, {"a": 1, "b": 2}.values(), DOES_NOT_RAISE),
    (True, "True", RAISES_ASSERTION),
    ("ings", "string", RAISES_ASSERTION),
    ("string", "string", DOES_NOT_RAISE),
    (get_singleton, get_singleton, RAISES_ASSERTION),
    (Person("John", 30), get_singleton, RAISES_ASSERTION),
])
def test_to_be_contained_in(expected, actual, context):
    with context:
        expect(expected).to.be_contained_in(actual)

    with context:
        expect(expected).to.be_in(actual)

    with context:
        expect(expected).to.be_included_in(actual)


@expected_params([
    ([], DOES_NOT_RAISE),
    ({}, DOES_NOT_RAISE),
    (set(), DOES_NOT_RAISE),
    ("", DOES_NOT_RAISE),
    (tuple(), DOES_NOT_RAISE),
    (range(0), DOES_NOT_RAISE),
    ("abcd", RAISES_ASSERTION),
    ({"a": 1, "b": 2}, RAISES_ASSERTION),
    ("True", RAISES_ASSERTION),
    ([1, 2], RAISES_ASSERTION),
    ({1, 2}, RAISES_ASSERTION),
    ((1, 3), RAISES_ASSERTION),
    (1, RAISES_ASSERTION),
    (range(100), RAISES_ASSERTION),
])
def test_to_be_empty(expected, context):
    with context:
        expect(expected).to.be_empty()


@expected_params([
    (True, DOES_NOT_RAISE),
    (1, RAISES_ASSERTION),
    (False, RAISES_ASSERTION),
    ([], RAISES_ASSERTION),
    (get_singleton, RAISES_ASSERTION),
])
def test_to_be_true(expected, context):
    with context:
        expect(expected).to.be_true()


@expected_params([
    (True, RAISES_ASSERTION),
    (0, RAISES_ASSERTION),
    (False, DOES_NOT_RAISE),
    ([], RAISES_ASSERTION),
    (get_singleton, RAISES_ASSERTION),
])
def test_to_be_false(expected, context):
    with context:
        expect(expected).to.be_false()


@expected_params([
    (True, DOES_NOT_RAISE),
    (1, DOES_NOT_RAISE),
    (get_singleton, DOES_NOT_RAISE),
    ([1], DOES_NOT_RAISE),
    ([], RAISES_ASSERTION),
    (0, RAISES_ASSERTION),
    (False, RAISES_ASSERTION),
])
def test_to_be_truthy(expected, context):
    with context:
        expect(expected).to.be_truthy()


@expected_params([
    (True, RAISES_ASSERTION),
    (1, RAISES_ASSERTION),
    (get_singleton, RAISES_ASSERTION),
    ([1], RAISES_ASSERTION),
    ([], DOES_NOT_RAISE),
    (0, DOES_NOT_RAISE),
    (False, DOES_NOT_RAISE),
])
def test_to_be_falsey(expected, context):
    with context:
        expect(expected).to.be_falsey()


@expected_actual_params([
    ([1], list, DOES_NOT_RAISE),
    (2, int, DOES_NOT_RAISE),
    ("a", str, DOES_NOT_RAISE),
    ({"a", "b"}, set, DOES_NOT_RAISE),
    ({"a": 1, "b": 2}, dict, DOES_NOT_RAISE),
    (True, bool, DOES_NOT_RAISE),
    (Person("John", 30), Person, DOES_NOT_RAISE),
    (1, int, DOES_NOT_RAISE),
    (1.0, float, DOES_NOT_RAISE),
    (Person("John", 30), object, RAISES_ASSERTION),
    ("string", "ings", RAISES_ASSERTION),
    ("string", int, RAISES_ASSERTION),
    (1, str, RAISES_ASSERTION),
    (1, float, RAISES_ASSERTION),
    (1.0, int, RAISES_ASSERTION),
])
def test_to_be_of_type(expected, actual, context):
    with context:
        expect(expected).to.be_of_type(actual)


@expected_actual_params([
    ([1], list, DOES_NOT_RAISE),
    (2, int, DOES_NOT_RAISE),
    ("a", str, DOES_NOT_RAISE),
    ({"a", "b"}, set, DOES_NOT_RAISE),
    ({"a": 1, "b": 2}, dict, DOES_NOT_RAISE),
    (True, bool, DOES_NOT_RAISE),
    (Person("John", 30), Person, DOES_NOT_RAISE),
    (Person("John", 30), object, DOES_NOT_RAISE),
    (1, int, DOES_NOT_RAISE),
    (1.0, float, DOES_NOT_RAISE),
    ("string", "ings", RAISES_ASSERTION),
    ("string", int, RAISES_ASSERTION),
    (1, str, RAISES_ASSERTION),
    (1, float, RAISES_ASSERTION),
    (1.0, int, RAISES_ASSERTION),
])
def test_to_inherit(expected, actual, context):
    with context:
        expect(expected).to.inherit(actual)


# TODO: copy to expect_to_not_test_suite


@expected_actual_params([
    (1, 2, RAISES_ASSERTION),
    (3, 2, DOES_NOT_RAISE),
    (3.2, 1, DOES_NOT_RAISE),
    (100.1, 100.2, RAISES_ASSERTION),
    ([1, 2], [1, 2, 3], RAISES_ASSERTION),
    ([1], [2], RAISES_ASSERTION),
    (2, 2, RAISES_ASSERTION),
])
def test_to_be_greater_than(expected, actual, context):
    with context:
        expect(expected).to.be_greater_than(actual)


@expected_actual_params([
    (1, 2, DOES_NOT_RAISE),
    (3, 2, RAISES_ASSERTION),
    (3.2, 1, RAISES_ASSERTION),
    (100.1, 100.2, DOES_NOT_RAISE),
    ([1, 2], [1, 2, 3], DOES_NOT_RAISE),
    ([1], [2], DOES_NOT_RAISE),
    (2, 2, RAISES_ASSERTION),
])
def test_to_be_lesser_than(expected, actual, context):
    with context:
        expect(expected).to.be_lesser_than(actual)


@expected_actual_params([
    (1, 2, RAISES_ASSERTION),
    (3, 2, DOES_NOT_RAISE),
    (3.2, 1, DOES_NOT_RAISE),
    (100.1, 100.2, RAISES_ASSERTION),
    ([1, 2], [1, 2, 3], RAISES_ASSERTION),
    ([1], [2], RAISES_ASSERTION),
    (2, 2, DOES_NOT_RAISE),
])
def test_to_be_greater_or_equal_to(expected, actual, context):
    with context:
        expect(expected).to.be_greater_or_equal_to(actual)


@expected_actual_params([
    (1, 2, DOES_NOT_RAISE),
    (3, 2, RAISES_ASSERTION),
    (3.2, 1, RAISES_ASSERTION),
    (100.1, 100.2, DOES_NOT_RAISE),
    ([1, 2], [1, 2, 3], DOES_NOT_RAISE),
    ([1], [2], DOES_NOT_RAISE),
    (2, 2, DOES_NOT_RAISE),
])
def test_to_be_lesser_or_equal_to(expected, actual, context):
    with context:
        expect(expected).to.be_lesser_or_equal_to(actual)


@expected_params([
    (1, DOES_NOT_RAISE),
    (3, DOES_NOT_RAISE),
    (3.2, DOES_NOT_RAISE),
    ("a", RAISES_ASSERTION),
    ([1, 2], RAISES_ASSERTION),
    (set(), RAISES_ASSERTION),
    (tuple(), RAISES_ASSERTION),
    ("123", DOES_NOT_RAISE),
    (lambda x: x, RAISES_ASSERTION),
    (Person("Fero", 12), RAISES_ASSERTION),
])
def test_to_be_numeric(expected, context):
    with context:
        expect(expected).to.be_numeric()


@expected_params([
    (1, DOES_NOT_RAISE),
    (3, DOES_NOT_RAISE),
    (3.2, DOES_NOT_RAISE),
    ("a", RAISES_ASSERTION),
    ([1, 2], RAISES_ASSERTION),
    (set(), RAISES_ASSERTION),
    (tuple(), RAISES_ASSERTION),
    ("123", RAISES_ASSERTION),
    (lambda x: x, RAISES_ASSERTION),
    (Person("Fero", 12), RAISES_ASSERTION),
])
def test_to_be_strictly_numeric(expected, context):
    with context:
        expect(expected).to.be_numeric(strict=True)


@expected_params([
    (1, RAISES_ASSERTION),
    ("a", RAISES_ASSERTION),
    ([1, 2], RAISES_ASSERTION),
    (set(), RAISES_ASSERTION),
    (tuple(), RAISES_ASSERTION),
    (lambda x: x, DOES_NOT_RAISE),
    (Person, DOES_NOT_RAISE),
])
def test_to_be_callable(expected, context):
    with context:
        expect(expected).to.be_callable()


@expected_params([
    ('', RAISES_ASSERTION),
    (0, RAISES_ASSERTION),
    (False, RAISES_ASSERTION),
    ([], RAISES_ASSERTION),
    (None, DOES_NOT_RAISE),
])
def test_to_be_none(expected, context):
    with context:
        expect(expected).to.be_none()


@expected_params([
    ('', DOES_NOT_RAISE),
    (r'hello', DOES_NOT_RAISE),
    (0, RAISES_ASSERTION),
    (False, RAISES_ASSERTION),
    ([], RAISES_ASSERTION),
    (None, RAISES_ASSERTION),
])
def test_to_be_str(expected, context):
    with context:
        expect(expected).to.be_str()


@expected_params([
    ('', RAISES_ASSERTION),
    (0, RAISES_ASSERTION),
    (1, RAISES_ASSERTION),
    (False, DOES_NOT_RAISE),
    (True, DOES_NOT_RAISE),
    ([], RAISES_ASSERTION),
    (None, RAISES_ASSERTION),
])
def test_to_be_bool(expected, context):
    with context:
        expect(expected).to.be_bool()


@expected_params([
    (0, DOES_NOT_RAISE),
    (-1, DOES_NOT_RAISE),
    (0.0, RAISES_ASSERTION),
    (-10.1, RAISES_ASSERTION),
])
def test_to_be_int(expected, context):
    with context:
        expect(expected).to.be_int()


@expected_params([
    (0, RAISES_ASSERTION),
    (-1, RAISES_ASSERTION),
    (0.0, DOES_NOT_RAISE),
    (-10.1, DOES_NOT_RAISE),
])
def test_to_be_float(expected, context):
    with context:
        expect(expected).to.be_float()


@expected_params([
    ('', RAISES_ASSERTION),
    ([], DOES_NOT_RAISE),
    ([1], DOES_NOT_RAISE),
    ((1,), RAISES_ASSERTION),
])
def test_to_be_list(expected, context):
    with context:
        expect(expected).to.be_list()
