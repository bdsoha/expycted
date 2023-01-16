from __future__ import annotations

from typing import Any

from expycted.core.matchers import BaseMatcher


class InheritMatcher(BaseMatcher):
    """Asserts the actual value inherits from expected value."""

    def _matches(self, *, expected: Any) -> bool:
        try:
            return isinstance(self._expectation.actual, expected)
        except Exception:
            return False
