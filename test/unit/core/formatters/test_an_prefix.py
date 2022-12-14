from __future__ import annotations

from expycted.core.formatters import AnPrefix


def test_starts_with_a_vowel():
    assert AnPrefix.format("a") == "an"
    assert AnPrefix.format("e") == "an"
    assert AnPrefix.format("i") == "an"
    assert AnPrefix.format("o") == "an"
    assert AnPrefix.format("u") == "an"


def test_does_not_start_with_a_vowel():
    assert AnPrefix.format("b") == "a"
    assert AnPrefix.format("c") == "a"
    assert AnPrefix.format("d") == "a"
    assert AnPrefix.format("f") == "a"
    assert AnPrefix.format("g") == "a"


def test_get_first_letter_in_sequence():
    assert AnPrefix.format("1234a") == "an"
    assert AnPrefix.format("1234b") == "a"


def test_non_str_values():
    assert AnPrefix.format(list) == "a"


def test_capital_letters():
    assert AnPrefix.format("`Iterable`") == "an"
