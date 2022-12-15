from __future__ import annotations

from typing import Any

from expycted.core.matchers import BaseMatcher


class EqualMatcher(BaseMatcher):
    """Asserts that two variables have the same value."""

    OPERATION = "=="

    def _matches(self, *, expected: Any) -> bool:
        return self._expectation.actual == expected
