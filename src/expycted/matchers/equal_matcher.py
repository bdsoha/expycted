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

        check_callbacks = [
            lambda: str(self._expectation.actual) == str(expected),
            lambda: pickle.dumps(self._expectation.actual) == pickle.dumps(expected),
            lambda: self._expectation.actual == expected,
        ]

        return any(check() for check in check_callbacks)
