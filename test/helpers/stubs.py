# pylint: skip-file

from __future__ import annotations

from enum import Enum

from helpers.utils import DescribedParam


class Parent:
    pass


class Person(Parent):
    def __init__(self, first_name="John", last_name="Doe"):
        self.first_name = first_name
        self.last_name = last_name


class PersonSameStr(Person):
    def __str__(self):
        return "same"


class PersonDifferentStr(Person):
    def __str__(self):
        from random import random

        return str(random())


class Day(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


EMPTY_LIST = DescribedParam([], description="Empty list")
EMPTY_SET = DescribedParam(set(), description="Empty set")
EMPTY_STRING = DescribedParam("", description="Empty string")
EMPTY_BSTRING = DescribedParam(b"", description="Empty byte string")
EMPTY_TUPLE = DescribedParam(tuple(), description="Empty tuple")
EMPTY_DICT = DescribedParam({}, description="Empty dict")
EMPTY_RANGE = lambda: DescribedParam(range(0), description="Empty range")
EMPTY_GENERATOR = lambda: DescribedParam(
    (i for i in range(0)),
    description="Empty generator",
)

INT = DescribedParam(1, description="Example int")
ZERO = DescribedParam(0, description="Literal 0")
INT_STR = DescribedParam("1", description="Integer value as string")
FLOAT = DescribedParam(1.1, description="Example float")
FLOAT_STR = DescribedParam("1.1", description="Float value as string")
FUNCTION_BUILT = DescribedParam(print, description="Built-in function")
LIST = DescribedParam([1, "hello", "world"], description="Example list")
SET = DescribedParam({1, "hello", "world"}, description="Example set")
STRING = DescribedParam("hello world", description="Example string")
BSTRING = DescribedParam(b"hello world", description="Example byte string")
TUPLE = DescribedParam((1, "hello", "world"), description="Example tuple")
DICT = DescribedParam({1: "hello world"}, description="Example dict")
RANGE = lambda: DescribedParam(range(1), description="Example range")
GENERATOR = lambda: DescribedParam(
    (i for i in range(1)), description="Example generator"
)
SINGLETON_OBJECT = DescribedParam(Person(), description="Singleton object")
NOT_SINGLETON_OBJECT = lambda: DescribedParam(
    Person(),
    description="Not singleton object",
)

PERSON_SAME_STR = lambda: PersonSameStr()
PERSON_DIFFERENT_STR = lambda: PersonSameStr()

#### OLD

PERSON = Person()

FALSE_NONE_EQUIVALENT = (False, None, "False None equivalent")

TRUE_STR_EQUIVALENT = (True, "True", "bool (True) str equivalent")
FALSE_STR_EQUIVALENT = (False, "False", "bool (False) str equivalent")

INT_STR_EQUIVALENT = (1, "1", "int str equivalent")

BYTE_STR_EQUIVALENT = (b"hello", "hello", "byte-str str equivalent")

LIST_TUPLE_EQUIVALENT = ([True, 1.1], (True, 1.1), "list tuple equivalent")

SAME_OBJECT = (PERSON, PERSON, "same object in memory")
COPY_OBJECT = (Person(), Person(), "copied object")

CONTAIN = (
    ([2], 2, "list"),
    ({"a", "b"}, "a", "set"),
    ("abcd", "bc", "substr"),
    ("abcd", "", "empty str"),
    ({"a": 1, "b": 2}, "a", "dict"),
    ("string", "string", "full str"),
)

NOT_CONTAIN = (
    ([1], 2, "list"),
    (["a", 2], ["a"], "item in list"),
    ("string", "ings", "str"),
    ({"a": 1, "b": 2}, "c", "dict"),
)

CONTAIN_TYPE_ERROR = (
    ("hello2", 2, "int in str"),
    TRUE_STR_EQUIVALENT,
    COPY_OBJECT,
    SAME_OBJECT,
)
