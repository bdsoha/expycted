from enum import Enum
from expycted.core.formatters import StringOutputFormatter
from helpers.stubs import PERSON, Day

import pytest


@pytest.mark.parametrize("actual,formatted", [
    (True, "True"),
    (5, "5"),
    (5.5, "5.5"),
    ("5", "\"5\""),
    (b"5", "b\"5\""),
    ([1,2], "[1, 2]"),
    (print, "builtins.print"),
    (type(int), "builtins.type"),
    (int, "builtins.int"),
    (Enum, "enum.Enum"),
    (PERSON.__class__, "helpers.stubs.Person"),
    (Day.SUNDAY, "helpers.stubs.Day.SUNDAY"),
])
def test_builtin_types(actual, formatted):
    assert StringOutputFormatter.format(actual) == formatted

def test_instance_type():
    assert StringOutputFormatter.format(PERSON).startswith("helpers.stubs.Person@0x")
