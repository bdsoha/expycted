from enum import Enum


class Parent:
    pass


class Person(Parent):
    def __init__(self, first_name="John", last_name="Doe"):
        self.first_name = first_name
        self.last_name = last_name


class Day(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURDAY = 5
    FRIDAY = 6
    SATURDAY = 7


PERSON = Person()

TRUE_INT_EQUIVALENT = (True, 1, "True int equivalent")
FALSE_INT_EQUIVALENT = (False, 0, "False int equivalent")
FALSE_NONE_EQUIVALENT = (False, None, "False None equivalent")

TRUE_STR_EQUIVALENT = (True, "True", "bool (True) str equivalent")
FALSE_STR_EQUIVALENT = (False, "False", "bool (False) str equivalent")

INT_STR_EQUIVALENT = (1, "1", "int str equivalent")
INT_FLOAT_EQUIVALENT = (1, 1.0, "int float equivalent")

RSTR_STR_EQUIVALENT = (r"hello","hello", "r-str str equivalent")
BYTE_STR_EQUIVALENT = (b"hello","hello", "byte-str str equivalent")

LIST_TUPLE_EQUIVALENT = ([True, 1.1], (True, 1.1), "list tuple equivalent")

SAME_OBJECT = (PERSON, PERSON, "same object in memory")
COPY_OBJECT = (Person(), Person(), "copied object")


EQUAL = (
    TRUE_INT_EQUIVALENT,
    FALSE_INT_EQUIVALENT,
    INT_FLOAT_EQUIVALENT,
    RSTR_STR_EQUIVALENT,
    SAME_OBJECT,
    (True, True, "bool"),
    (1, 1, "int"),
    (1.1, 1.1, "float"),
    ("hello", "hello", "str"),
    ([True, 1.1], [True, 1.1], "list"),
    ({True, 1.1}, {1.1, True}, "set ignore order"),
    ({"a": [True, 1.1]}, {"a": [True, 1.1]}, "dict"),
)

NOT_EQUAL = (
    TRUE_STR_EQUIVALENT,
    FALSE_STR_EQUIVALENT,
    INT_STR_EQUIVALENT,
    COPY_OBJECT,
    LIST_TUPLE_EQUIVALENT,
    FALSE_NONE_EQUIVALENT,
    BYTE_STR_EQUIVALENT,
)

BE = (
    *EQUAL,
    TRUE_STR_EQUIVALENT,
    FALSE_STR_EQUIVALENT,
    INT_STR_EQUIVALENT,
    COPY_OBJECT
)

NOT_BE = (
    LIST_TUPLE_EQUIVALENT,
    FALSE_NONE_EQUIVALENT,
    BYTE_STR_EQUIVALENT,
)

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
    SAME_OBJECT
)

EMPTY = (
    [],
    {},
    set(),
    "",
    tuple(),
)

def EMPTY_GENERATORS():
    return (
        range(0),
        (i for i in range(0))
    )

NOT_EMPTY = (
    " ",
    {"a": 1},
    [1],
    {1},
    (1,),
    range(100),
    (i for i in range(10))
)

NOT_EMPTY_TYPE_ERROR = (
    0,
    True,
    100,
    PERSON,
)

TRUE = (True,)

NOT_TRUE = (
    False,
    1,
    "True"
)

FALSE = (False,)

NOT_FALSE = (
    True,
    0,
    "False"
)

TRUETHY = (
    *TRUE,
    *NOT_EMPTY,
    1,
    "True"
    "False",
    PERSON
)

NOT_TRUETHY = (
    *FALSE,
    *EMPTY
)

FALSEY = (
    *FALSE,
    *EMPTY,
    0,
)

NOT_FALSEY = (
    *TRUE,
    *NOT_EMPTY,
    PERSON
)

TYPE = (
    ([1], list),
    (2, int),
    ("a", str),
    ({"a", "b"}, set),
    ({"a": 1, "b": 2}, dict),
    (True, bool),
    (PERSON, Person),
    (1, int),
    (1.0, float),
    (type(PERSON), type),
)

NOT_TYPE = (
    (PERSON, Parent),
    (PERSON, object),
    ("string", "ings"),
    ("string", int),
    (1, str),
    (1, float),
    (1.0, int),
)

INHERIT = (
    *TYPE,
    (1, object),
    (1, object),
    (1.0, object),
    (PERSON, Parent),
    (PERSON, object),
)

NOT_INHERIT = (
    ("string", int),
    (1, str),
    (1, float),
    (1.0, int),
)

INHERIT_TYPE_ERROR = (
    ("string", "str"),
)

GREATER_THAN = (
    (3, 2),
    (3.2, 3),
    ([2], [1]),
    ([1, 0], [1]),
)

LESS_THAN = (
    (2, 3),
    (3, 3.2),
    ([1], [2]),
    ([1], [1, 0]),
)

GREATER_THAN_OR_EQUAL = (
    *GREATER_THAN,
    (1, 1.0),
    ([1], [1])
)

LESS_THAN_OR_EQUAL = (
    *LESS_THAN,
    (1, 1.0),
    ([1], [1])
)

NUMERIC = (
    1,
    "1",
    3,
    3.2,
    "3.2",
    1e1,
    "1e1",
    1_001_123,
    "1_001_123"
)

NOT_NUMERIC = (
    True,
    False,
    "a",
    [1, 2],
    set(),
    tuple(),
    lambda x: x,
    PERSON
)