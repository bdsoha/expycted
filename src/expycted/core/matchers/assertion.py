from __future__ import annotations

from functools import wraps
from typing import Callable, Type, Union

from .base_matcher import BaseMatcher
from .matcher_proxy import MatcherProxy


def assertion(callback: Callable) -> Callable:
    """Decorate assertion method with a matcher."""

    @wraps(callback)
    def _wrapper(proxy):
        instance: Union[Type[BaseMatcher], BaseMatcher] = callback(proxy)

        if not isinstance(instance, BaseMatcher):
            instance = instance(proxy)

        return MatcherProxy(instance)

    return _wrapper
