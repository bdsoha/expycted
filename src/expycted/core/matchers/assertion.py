from typing import Callable, Type
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


class AssertionAlias:
    """Decorate aliases of an assertion method."""

    def __init__(self, alias: str):
        self._alias = alias

    def __call__(self, callback: Callable) -> Callable:
        def _wrapper(proxy):
            callback(proxy)

            return getattr(proxy, self._alias)

        return property(_wrapper)
