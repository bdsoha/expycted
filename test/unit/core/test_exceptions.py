from expycted.core.exceptions import MatcherError


def test_matcher_error():
    error = MatcherError(str)

    assert str(error) == "Matcher Error: recieved value must be a `str`"


def test_matcher_error_two_types():
    error = MatcherError(tuple, list)

    assert str(error) == "Matcher Error: recieved value must be a `list` or `tuple`"

def test_matcher_error_multiple_types_sorted():
    error = MatcherError(str, tuple, list)

    assert str(error) == "Matcher Error: recieved value must be a `list`, `str`, or `tuple`"

def test_matcher_error_with_an_instead_of_a():
    error = MatcherError(int)

    assert str(error) == "Matcher Error: recieved value must be an `int`"
