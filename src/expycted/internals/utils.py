from functools import wraps
from typing import Callable
import os


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


def assertion(fn: Callable) -> Callable:
    @hidetraceback
    @wraps(fn)
    def _(self, *args, **kwargs):
        fn(self, *args, **kwargs)

        return self._execute_internal_assertion(fn.__name__, *args, **kwargs)

    return _
