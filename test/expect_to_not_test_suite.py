import pytest
from expycted import expect


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


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, True),
    (1, 1, False),
    (1, 0, True),
    (0, 0, False),
    (True, 'True', True),
    (True, True, False),
    (True, False, True),
    ('string', 'another', True),
    ('string', 'string', False),
    (1, '1', True),
    (get_singleton, get_singleton, False),
    (get_singleton, Person("John", 30), True),
]
)
def test_to_not_equal(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.equal(v2)
    else:
        expect(v1).to_not.equal(v2)


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, True),
    (1, 1, False),
    (1, 0, True),
    (0, 0, False),
    (True, 'True', False),
    (True, True, False),
    (True, False, True),
    ('string', 'another', True),
    ('string', 'string', False),
    (1, '1', False),
    (get_singleton, get_singleton, False),
    (get_singleton, Person("John", 30), True),
    (1, 1.0, False),
    (2.0, 3, True)
]
)
def test_to_not_be(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be(v2)
    else:
        expect(v1).to_not.be(v2)


@pytest.mark.parametrize("v1,v2,true", [
    ([1], None, True),
    ([2], 2, False),
    (['a', 2], ['b'], True),
    (set(['a', 'b']), 'a', False),
    ('abcd', 'bc', False),
    ({'a': 1, 'b': 2}.values(), 2, False),
    ('True', True, False),
    ('string', 'ings', True),
    ('string', 'string', False),
]
)
def test_to_not_contain(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.contain(v2)
    else:
        expect(v1).to_not.contain(v2)


@pytest.mark.parametrize("v1,v2,true", [
    ([1], None, True),
    ([2], 2, False),
    (['a', 2], ['b'], True),
    (set(['a', 'b']), 'a', False),
    ('abcd', 'bc', False),
    ({'a': 1, 'b': 2}.values(), 2, False),
    ('True', True, False),
    ('string', 'ings', True),
    ('string', 'string', False),
    (get_singleton, get_singleton, False),
]
)
def test_to_not_be_contained_in(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v2).to_not.be_contained_in(v1)
    else:
        expect(v2).to_not.be_contained_in(v1)


@pytest.mark.parametrize("v1,true", [
    ([], False),
    ({}, False),
    (set([]), False),
    ('', False),
    ((), False),
    ('abcd', True),
    ({'a': 1, 'b': 2}, True),
    ('True', True),
    ([1, 2], True),
    (set([1, 2]), True),
    ((1, 3), True)
]
)
def test_to_not_be_empty(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_empty()
    else:
        expect(v1).to_not.be_empty()


@pytest.mark.parametrize("v1,true", [
    (True, False),
    (False, True),
    ([], True),
    (get_singleton, True),

]
)
def test_to_not_be_true(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_true()
    else:
        expect(v1).to_not.be_true()


@pytest.mark.parametrize("v1,true", [
    (True, True),
    (False, False),
    ([], True),
    (get_singleton, True),

]
)
def test_to_not_be_false(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_false()
    else:
        expect(v1).to_not.be_false()


@pytest.mark.parametrize("v1,true", [
    (True, False),
    (1, False),
    (get_singleton, False),
    ([1], False),
    ([], True),
    (0, True),
    (False, True)
]
)
def test_to_not_be_truthy(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_truthy()
    else:
        expect(v1).to_not.be_truthy()


@pytest.mark.parametrize("v1,true", [
    (True, True),
    (1, True),
    (get_singleton, True),
    ([1], True),
    ([], False),
    (0, False),
    (False, False)
]
)
def test_to_not_be_falsey(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_falsey()
    else:
        expect(v1).to_not.be_falsey()


@pytest.mark.parametrize("v1,v2,true", [
    ([1], list, False),
    (2, int, False),
    ('a', str, False),
    (set(['a', 'b']), set, False),
    ({'a': 1, 'b': 2}, dict, False),
    (True, bool, False),
    (Person("John", 30), Person, False),
    (1, int, False),
    (1.0, float, False),
    (Person("John", 30), object, True),
    ('string', 'ings', True),
    ('string', int, True),
    (1, str, True),
    (1, float, True),
    (1.0, int, True)
]
)
def test_to_not_be_of_type(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_of_type(v2)
    else:
        expect(v1).to_not.be_of_type(v2)


@pytest.mark.parametrize("v1,v2,true", [
    ([1], list, False),
    (2, int, False),
    ('a', str, False),
    (set(['a', 'b']), set, False),
    ({'a': 1, 'b': 2}, dict, False),
    (True, bool, False),
    (Person("John", 30), Person, False),
    (Person("John", 30), object, False),
    (1, int, False),
    (1.0, float, False),
    ('string', 'ings', False),
    ('string', int, True),
    (1, str, True),
    (1, float, True),
    (1.0, int, True)
]
)
def test_to_not_inherit(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.inherit(v2)
    else:
        expect(v1).to_not.inherit(v2)

# NUMERIC TESTS


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, True),
    (3, 2, False),
    (3.2, 1, False),
    (100.1, 100.2, True),
    ([1, 2], [1, 2, 3], True),
    ([1], [2], True),
    (2, 2, True),

]
)
def test_to_not_be_greater_than(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_greater_than(v2)
    else:
        expect(v1).to_not.be_greater_than(v2)


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, False),
    (3, 2, True),
    (3.2, 1, True),
    (100.1, 100.2, False),
    ([1, 2], [1, 2, 3], False),
    ([1], [2], False),
    (2, 2, True),

]
)
def test_to_not_be_lesser_than(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_lesser_than(v2)
    else:
        expect(v1).to_not.be_lesser_than(v2)


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, True),
    (3, 2, False),
    (3.2, 1, False),
    (100.1, 100.2, True),
    ([1, 2], [1, 2, 3], True),
    ([1], [2], True),
    (2, 2, False),

]
)
def test_to_not_be_greater_or_equal_to(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_greater_or_equal_to(v2)
    else:
        expect(v1).to_not.be_greater_or_equal_to(v2)


@pytest.mark.parametrize("v1,v2,true", [
    (1, 2, False),
    (3, 2, True),
    (3.2, 1, True),
    (100.1, 100.2, False),
    ([1, 2], [1, 2, 3], False),
    ([1], [2], False),
    (2, 2, False),

]
)
def test_to_not_be_lesser_or_equal_to(v1, v2, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_lesser_or_equal_to(v2)
    else:
        expect(v1).to_not.be_lesser_or_equal_to(v2)


@pytest.mark.parametrize("v1,true", [
    (1, False),
    (3, False),
    (3.2, False),
    ('a', True),
    ([1, 2], True),
    (set(), True),
    (tuple(), True),
    ('123', False),
    (lambda x: x, True),
    (Person('Fero', 12), True),
]
)
def test_to_not_be_numeric(v1, true):
    if not true:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_numeric()
    else:
        expect(v1).to_not.be_numeric()
