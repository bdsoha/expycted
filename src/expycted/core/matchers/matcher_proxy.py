from typing import Any

from wrapt import ObjectProxy


class MatcherProxy(ObjectProxy):
    """Override a matcher instance's ``__call__`` method."""

    def __call__(self, expected: Any = ...):
        results = self.__wrapped__.__call__(expected=expected)

        assert results, self.message().render(self._actual, expected=expected)
