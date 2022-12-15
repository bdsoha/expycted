from __future__ import annotations

from functools import wraps
from typing import Callable

from .base_matcher import BaseMatcher
from .matcher_proxy import MatcherProxy


def assertion(callback: Callable) -> Callable:
    """Decorate assertion method with a matcher."""

    @wraps(callback)
    def _wrapper(proxy):
        instance = callback(proxy)

        if not isinstance(instance, BaseMatcher):
            instance = instance(
                proxy.expected,
                negated=proxy.negate,
            )

        return MatcherProxy(instance)

    return _wrapper
