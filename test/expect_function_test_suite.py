import pytest

from expycted import expect


def raise_exception(exc_class: Exception):
    raise exc_class("test")


def do_nothing():
    pass


@pytest.mark.parametrize(
    "fn,arguments,exc_class,raises",
    [
        (lambda x: raise_exception(x), [ValueError], ValueError, True),
        (lambda x: raise_exception(x), [ValueError], TypeError, False),
        (lambda x: raise_exception(x), [ValueError], AssertionError, False),
        (lambda x: raise_exception(x), [TypeError], TypeError, True),
        (lambda: do_nothing, [], None, False),
        ("string".replace, ["ing", "ength"], None, False),
        ("string".replace, ["ing", "ength", "ele", "aa"], TypeError, True),
    ],
)
def test_fn_expect_raise(fn, arguments, exc_class, raises):
    if not raises:
        # Confusing test, if fn called with arguments doesn't raise exc_class then AssertionError is raised
        with pytest.raises(AssertionError):
            expect.function(fn).to_raise(exc_class).when_called_with(*arguments)
    else:
        expect.function(fn).to_raise(exc_class).when_called_with(*arguments)


@pytest.mark.parametrize(
    "fn, arguments, ret_value, ret_type, true",
    [
        (str, [10], "10", str, True),
        ("string".replace, ["ing", "ength"], "strength", None, True),
        (map, [lambda x: x + 1, [1, 2, 3]], None, map, True),
        (map, [lambda x: x + 1, [1, 2, 3]], None, list, False),
        ("string".replace, ["ing", "ength"], "strengt", None, False),
    ],
)
def test_fn_expect_return(fn, arguments, ret_value, ret_type, true):
    if not true:
        # Confusing test, if fn called with arguments doesn't raise exc_class then AssertionError is raised
        with pytest.raises(AssertionError):
            expect.function(fn).to_return(
                value=ret_value, type_of_value=ret_type
            ).when_called_with(*arguments)
    else:
        expect.function(fn).to_return(
            value=ret_value, type_of_value=ret_type
        ).when_called_with(*arguments)

def test_fn_raises_value_error_when_called_without_return():
    with pytest.raises(ValueError):
        expect.function(str).to_return().when_called_with([10])
