from functools import wraps
from typing import Callable

from .base_matcher import BaseMatcher
from .matcher_proxy import MatcherProxy


def assertion(callback: Callable) -> Callable:
    """Decorate assertion method with a matcher."""

    # @wraps(callback)
    def _wrapper(proxy):
        instance = callback(proxy)

        if not isinstance(instance, BaseMatcher):
            instance = instance(
                actual=proxy.expected,
                negated=proxy.negate,
            )

        return MatcherProxy(instance)

    return _wrapper


class AssertionAlias:
    """Decorate aliases of an assertion method."""

    def __init__(self, alias: str):
        self._alias = alias

    def __call__(self, callback: Callable) -> Callable:
        @wraps(callback)
        def _wrapper(proxy):
            callback(proxy)

            return getattr(proxy, self._alias)

        return property(_wrapper)
