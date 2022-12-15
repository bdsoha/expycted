from __future__ import annotations

from expycted.core.matchers import BaseMatcher


class TypeMatcher(BaseMatcher):
    """Assert that the actual type is equivalent to the expected type."""

    OPERATION = "type"

    def _matches(self, expected) -> bool:
        return type(self._expectation.actual) is expected
