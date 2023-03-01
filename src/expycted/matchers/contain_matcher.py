from __future__ import annotations

from typing import Any

from expycted.core.matchers import BaseMatcher


class ContainMatcher(BaseMatcher):
    """Asserts that expected value contain in actual value."""

    def _matches(self, *, expected: Any) -> bool:
        try:
            return expected in self._expectation.actual
        except Exception:
            return False
