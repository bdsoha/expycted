from __future__ import annotations

from typing import Any

from expycted.core.matchers import BaseMatcher


class ContainedInMatcher(BaseMatcher):
    """Asserts the actual value contains in the expected value."""

    def _matches(self, *, expected: Any) -> bool:
        try:
            return self._expectation.actual in expected
        except Exception:
            return False
