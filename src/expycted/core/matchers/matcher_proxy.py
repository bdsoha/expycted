from __future__ import annotations

from typing import Any, Generic, TypeVar

import wrapt

from .base_matcher import BaseMatcher

T = TypeVar("T", bound=BaseMatcher)


class MatcherProxy(wrapt.ObjectProxy, Generic[T]):
    """Override a matcher instance's ``__call__`` method."""

    def __call__(self: T, expected: Any = ...):  # type: ignore
        """Wrap the proxied matcher with an ``assert`` call."""

        results = self.__wrapped__.__call__(expected=expected)  # type: ignore

        assert results, self.message().render(
            self._expectation.actual,
            expected=expected,
        )

        self._expectation.qualifiers.clear()

        return self._expectation
