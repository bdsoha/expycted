from __future__ import annotations

from expycted.core.exceptions import MatcherError


def test_matcher_error():
    error = MatcherError(str, actual=float)

    assert str(error) == (
        "Matcher Error:\nReceived value must be a `str`.\nBut, a `float` was provided."
    )


def test_matcher_error_two_types():
    error = MatcherError(tuple, list, actual=str)

    assert str(error) == (
        "Matcher Error:"
        "\nReceived value must be a `list` or `tuple`.\nBut, a `str` was provided."
    )


def test_matcher_error_multiple_types_sorted():
    error = MatcherError(str, tuple, list, actual=float)

    assert str(error) == (
        "Matcher Error:"
        "\nReceived value must be a `list`, `str`, or `tuple`.\nBut, "
        "a `float` was provided."
    )


def test_matcher_error_with_an_instead_of_a():
    error = MatcherError(int, actual=float)

    assert str(error) == (
        "Matcher Error:"
        "\nReceived value must be an `int`.\nBut, a `float` was provided."
    )
