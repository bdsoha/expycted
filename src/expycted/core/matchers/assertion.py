from __future__ import annotations

from functools import wraps
from typing import Callable, Type, TypeVar, Union

from .base_matcher import BaseMatcher
from .matcher_proxy import MatcherProxy

T = TypeVar("T", bound=BaseMatcher)


def assertion(callback: Callable[..., Union[Type[T], T]]) -> Callable[..., T]:
    """Decorate assertion method with a matcher."""

    @wraps(callback)
    def _wrapper(proxy) -> T:
        instance = callback(proxy)

        if not isinstance(instance, BaseMatcher):
            instance = instance(proxy)  # type: ignore

        return MatcherProxy(instance)  # type: ignore

    return _wrapper
