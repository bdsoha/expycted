from typing import Callable, Optional, Type
from .base_matcher import BaseMatcher
from .matcher_proxy import factory


class Assertion:
    """Decorate assertion method with a matcher."""

    def __init__(self, matcher: Type[BaseMatcher], alias: Optional[str] = None):
        self._matcher = matcher
        self._alias = alias

    def __call__(self, callback: Callable) -> Callable:
        def _wrapper(proxy):
            callback(proxy)

            return factory(self._matcher)(
                actual=proxy.expected,
                negated=proxy.negate,
                alias=self._alias
            )

        return property(_wrapper)
