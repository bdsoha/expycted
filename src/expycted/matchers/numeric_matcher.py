from __future__ import annotations

from expycted.core.matchers import BaseMatcher


class NumericMatcher(BaseMatcher):
    """Asserts that the value is numeric."""

    def _matches(self, *, expected) -> bool:
        if type(self._expectation.actual) is str:

            try:
                float(self._expectation.actual)
                return True

            except Exception:
                return False

        return type(self._expectation.actual) in [int, float]
