from __future__ import annotations

from typing import Any
import pickle

from expycted.core.matchers import BaseMatcher


class EqualMatcher(BaseMatcher):
    """Asserts that two variables have the same value."""

    OPERATION = "=="

    def _matches(self, *, expected: Any) -> bool:
        if not self._expectation.qualifiers.weak:
            return self._expectation.actual == expected

        return any(
            [
                str(self._expectation.actual) == str(expected),
                pickle.dumps(self._expectation.actual) == pickle.dumps(expected),
                self._expectation.actual == expected,
            ]
        )
