from expycted import expect
import pytest


def raise_exception(exc_class: Exception):
    raise exc_class('test')


def do_nothing():
    pass


@pytest.mark.parametrize("fn,arguments,exc_class,raises", [
    (lambda x: raise_exception(x), [ValueError], ValueError, True),
    (lambda x: raise_exception(x), [ValueError], TypeError, False),
    (lambda x: raise_exception(x), [ValueError], AssertionError, False),
    (lambda x: raise_exception(x), [TypeError], TypeError, True),
    (lambda: do_nothing, [], None, False),
    ('string'.replace, ['ing', 'ength'], None, False),
    ('string'.replace, ['ing', 'ength', 'ele', 'aa'], TypeError, True)
])
def test_expect_raise(fn, arguments, exc_class, raises):
    if not raises:
        # Confusing test, if fn called with arguments doesnt raise exc_class then AssertionError is raised
        with pytest.raises(AssertionError):
            expect.function(fn).to_raise(
                exc_class).when_called_with(*arguments)
    else:
        expect.function(fn).to_raise(exc_class).when_called_with(*arguments)
