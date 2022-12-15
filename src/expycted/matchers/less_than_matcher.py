from __future__ import annotations

from typing import Any

from expycted.core.matchers import BaseMatcher


class LessThanMatcher(BaseMatcher):
    """Asserts the actual value is less than the expected value."""

    def _matches(self, *, expected: Any) -> bool:
        if self._expectation.qualifiers.or_equal:
            return self._expectation.actual <= expected

        return self._expectation.actual < expected
