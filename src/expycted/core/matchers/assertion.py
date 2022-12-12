from typing import Callable, Optional, Type
from .base_matcher import BaseMatcher
from .matcher_proxy import factory


class Assertion:
    """Decorate assertion method with a matcher."""

    def __init__(self, matcher: Type[BaseMatcher], **kwargs):
        self._matcher = matcher
        self._kwargs = kwargs

    def __call__(self, callback: Callable) -> Callable:
        def _wrapper(proxy):
            callback(proxy)

            return factory(self._matcher)(
                actual=proxy.expected,
                negated=proxy.negate,
                alias=self._kwargs.pop("alias", callable.__name__),
                **self._kwargs
            )

        return property(_wrapper)
