from __future__ import annotations

from typing import Any
import pickle

from expycted.core.matchers import BaseMatcher


class EqualMatcher(BaseMatcher):
    """Asserts that two variables have the same value."""

    OPERATION = "=="

    def _str_check(self, expected):
        return str(self._expectation.actual) == str(expected)

    def _pickle_check(self, expected):
        return pickle.dumps(self._expectation.actual) == pickle.dumps(expected)

    def _equal_check(self, expected):
        return self._expectation.actual == expected

    def _matches(self, *, expected: Any) -> bool:
        if not self._expectation.qualifiers.weak:
            return self._equal_check(expected)

        check_callbacks = [
            lambda: self._str_check(expected),
            lambda: self._pickle_check(expected),
            lambda: self._equal_check(expected),
        ]

        return any(check() for check in check_callbacks)
