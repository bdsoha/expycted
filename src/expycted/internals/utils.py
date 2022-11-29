import os
from functools import wraps
from typing import Callable


def hidetraceback(fn: Callable) -> Callable:
    """Decorate helper methods to ignore internal assertion traceback

    Args:
        fn (Callable): Function to decorate

    Returns:
        Callable: The decorated function
    """
    @wraps(fn)
    def _(*args, **kwargs):
        fn.__globals__['__tracebackhide__'] = os.getenv('EXPYCTED_HIDETRACEBACK', True)
        return fn(*args, **kwargs)

    return _

def to_not_fn(fn: Callable) -> Callable:
    """Returns a function that negates the result of the provided function

    Args:
        fn (Callable): Function to negate
        *args: Arguments to pass to the function

    Returns:
        Callable: Negated function
    """
    @wraps(fn)
    def to_not_fn_inner(*args, **kwargs):
        res = fn(*args, **kwargs)
        assert not res[0], res[1].replace("to", "to not")

    return hidetraceback(to_not_fn_inner)
