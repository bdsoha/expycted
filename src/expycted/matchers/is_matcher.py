from __future__ import annotations

from expycted.core.matchers import BaseMatcher


class IsMatcher(BaseMatcher):
    """Asserts that the actual value is the expected value."""

    OPERATION = "is"

    def _matches(self, expected) -> bool:
        return self._expectation.actual is expected
