from expycted.core.exceptions import MatcherError


def test_matcher_error():
    error = MatcherError(float, str)

    assert str(error) == (
        "Matcher Error:\nReceived value must be a `str`.\nBut, a `float` was provided."
    )


def test_matcher_error_two_types():
    error = MatcherError(str, tuple, list)

    assert str(error) == (
        "Matcher Error:\nReceived value must be a `list` or `tuple`.\nBut, a `str` was provided."
    )


def test_matcher_error_multiple_types_sorted():
    error = MatcherError(float, str, tuple, list)

    assert str(error) == (
        "Matcher Error:"
        "\nReceived value must be a `list`, `str`, or `tuple`.\nBut, a `float` was provided."
    )


def test_matcher_error_with_an_instead_of_a():
    error = MatcherError(float, int)

    assert (
        str(error)
        == "Matcher Error:\nReceived value must be an `int`.\nBut, a `float` was provided."
    )
