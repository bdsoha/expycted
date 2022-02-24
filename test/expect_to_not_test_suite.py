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


@pytest.mark.parametrize("v1,v2,raised", [
    (1, 2, False),
    (1, 1, True),
    (1, 0, False),
    (0, 0, True),
    (True, 'True', False),
    (True, True, True),
    (True, False, False),
    ('string', 'another', False),
    ('string', 'string', True),
    (1, '1', False),
    (get_singleton, get_singleton, True),
    (get_singleton, Person("John", 30), False),
]
)
def test_to_equal(v1, v2, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.equal(v2)
    else:
        expect(v1).to_not.equal(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    (1, 2, False),
    (1, 1, True),
    (1, 0, False),
    (0, 0, True),
    (True, 'True', True),
    (True, True, True),
    (True, False, False),
    ('string', 'another', False),
    ('string', 'string', True),
    (1, '1', True),
    (get_singleton, get_singleton, True),
    (get_singleton, Person("John", 30), False),
]
)
def test_to_be(v1, v2, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be(v2)
    else:
        expect(v1).to_not.be(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], None, False),
    ([2], 2, True),
    (['a', 2], ['b'], False),
    (set(['a', 'b']), 'a', True),
    ('abcd', 'bc', True),
    ({'a': 1, 'b': 2}.values(), 2, True),
    ('True', True, True),
    ('string', 'ings', False),
    ('string', 'string', True),
]
)
def test_to_contain(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to_not.contain(v2)
    else:
        expect(v1).to_not.contain(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], None, False),
    ([2], 2, True),
    (['a', 2], ['b'], False),
    (set(['a', 'b']), 'a', True),
    ('abcd', 'bc', True),
    ({'a': 1, 'b': 2}.values(), 2, True),
    ('True', True, True),
    ('string', 'ings', False),
    ('string', 'string', True),
    (get_singleton, get_singleton, True),
]
)
def test_to_be_contained_in(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v2).to_not.be_contained_in(v1)
    else:
        expect(v2).to_not.be_contained_in(v1)


@pytest.mark.parametrize("v1,raised", [
    ([], True),
    ({}, True),
    (set([]), True),
    ('', True),
    ((), True),
    ('abcd', False),
    ({'a': 1, 'b': 2}, False),
    ('True', False),
    ([1, 2], False),
    (set([1, 2]), False),
    ((1, 3), False)
]
)
def test_to_be_empty(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_empty()
    else:
        expect(v1).to_not.be_empty()


@pytest.mark.parametrize("v1,raised", [
    (True, True),
    (False, False),
    ([], False),
    (get_singleton, False),

]
)
def test_to_be_true(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_true()
    else:
        expect(v1).to_not.be_true()


@pytest.mark.parametrize("v1,raised", [
    (True, False),
    (False, True),
    ([], False),
    (get_singleton, False),

]
)
def test_to_be_false(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_false()
    else:
        expect(v1).to_not.be_false()


@pytest.mark.parametrize("v1,raised", [
    (True, True),
    (1, True),
    (get_singleton, True),
    ([1], True),
    ([], False),
    (0, False),
    (False, False)
]
)
def test_to_be_truthy(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_truthy()
    else:
        expect(v1).to_not.be_truthy()


@pytest.mark.parametrize("v1,raised", [
    (True, False),
    (1, False),
    (get_singleton, False),
    ([1], False),
    ([], True),
    (0, True),
    (False, True)
]
)
def test_to_be_falsey(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to_not.be_falsey()
    else:
        expect(v1).to_not.be_falsey()


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], list, True),
    (2, int, True),
    ('a', str, True),
    (set(['a', 'b']), set, True),
    ({'a': 1, 'b': 2}, dict, True),
    (True, bool, True),
    (Person("John", 30), Person, True),
    (1, int, True),
    (1.0, float, True),
    (Person("John", 30), object, False),
    ('string', 'ings', False),
    ('string', int, False),
    (1, str, False),
    (1, float, False),
    (1.0, int, False)
]
)
def test_to_be_of_type(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to_not.be_of_type(v2)
    else:
        expect(v1).to_not.be_of_type(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], list, True),
    (2, int, True),
    ('a', str, True),
    (set(['a', 'b']), set, True),
    ({'a': 1, 'b': 2}, dict, True),
    (True, bool, True),
    (Person("John", 30), Person, True),
    (Person("John", 30), object, True),
    (1, int, True),
    (1.0, float, True),
    ('string', 'ings', True),
    ('string', int, False),
    (1, str, False),
    (1, float, False),
    (1.0, int, False)
]
)
def test_to_inherit(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to_not.inherit(v2)
    else:
        expect(v1).to_not.inherit(v2)
