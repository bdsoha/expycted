from __future__ import annotations

from functools import wraps
from typing import Callable


def chain(callback: Callable) -> Callable:
    @wraps(callback)
    def _wrapper(proxy):
        callback(proxy)

        return proxy

    return _wrapper
