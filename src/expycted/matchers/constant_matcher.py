from __future__ import annotations

from expycted.core.matchers import BaseMatcher


class ConstantMatcher(BaseMatcher):
    """Asserts that the actual value is the to match value."""

    OPERATION = "is"

    def _matches(self, expected) -> bool:
        return self._expectation.actual is self._to_match
