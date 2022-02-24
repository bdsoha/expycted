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
def test_to_equal(v1, v2, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.equal(v2)
    else:
        expect(v1).to.equal(v2)


@pytest.mark.parametrize("v1,v2,raised", [
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
]
)
def test_to_be(v1, v2, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be(v2)
    else:
        expect(v1).to.be(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], None, True),
    ([2], 2, False),
    (['a', 2], ['b'], True),
    (set(['a', 'b']), 'a', False),
    ('abcd', 'bc', False),
    ({'a': 1, 'b': 2}.values(), 2, False),
    ('True', True, True),
    ('string', 'ings', True),
    ('string', 'string', False),
    (get_singleton, get_singleton, True),
    (get_singleton, Person("John", 30), True),
]
)
def test_to_contain(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to.contain(v2)
    else:
        expect(v1).to.contain(v2)


@pytest.mark.parametrize("v1,v2,raised", [
    ([1], None, True),
    ([2], 2, False),
    (['a', 2], ['b'], True),
    (set(['a', 'b']), 'a', False),
    ('abcd', 'bc', False),
    ({'a': 1, 'b': 2}.values(), 2, False),
    ('True', True, True),
    ('string', 'ings', True),
    ('string', 'string', False),
    (get_singleton, get_singleton, True),
    (get_singleton, Person("John", 30), True),
]
)
def test_to_be_contained_in(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v2).to.be_contained_in(v1)
    else:
        expect(v2).to.be_contained_in(v1)


@pytest.mark.parametrize("v1,raised", [
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
def test_to_be_empty(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be_empty()
    else:
        expect(v1).to.be_empty()


@pytest.mark.parametrize("v1,raised", [
    (True, False),
    (False, True),
    ([], True),
    (get_singleton, True),

]
)
def test_to_be_true(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be_true()
    else:
        expect(v1).to.be_true()


@pytest.mark.parametrize("v1,raised", [
    (True, True),
    (False, False),
    ([], True),
    (get_singleton, True),

]
)
def test_to_be_false(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be_false()
    else:
        expect(v1).to.be_false()


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
def test_to_be_truthy(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be_truthy()
    else:
        expect(v1).to.be_truthy()


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
def test_to_be_falsey(v1, raised):
    if raised:
        with pytest.raises(AssertionError):
            expect(v1).to.be_falsey()
    else:
        expect(v1).to.be_falsey()


@pytest.mark.parametrize("v1,v2,raised", [
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
def test_to_be_of_type(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to.be_of_type(v2)
    else:
        expect(v1).to.be_of_type(v2)


@pytest.mark.parametrize("v1,v2,raised", [
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
    ('string', 'ings', True),
    ('string', int, True),
    (1, str, True),
    (1, float, True),
    (1.0, int, True)
]
)
def test_to_binherit(v1, v2, raised):
    if raised:
        with pytest.raises((AssertionError, TypeError)):
            expect(v1).to.inherit(v2)
    else:
        expect(v1).to.inherit(v2)
