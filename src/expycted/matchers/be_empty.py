from __future__ import annotations

from typing import Iterable

from expycted.core.matchers import BaseMatcher


class BeEmptyMatcher(BaseMatcher):
    """Asserts that the value is empty."""

    ALLOWED_TYPES = (Iterable,)
    MESSAGE = "Expected {actual} {to} be empty, but it was not."

    def _matches(self, *, expected) -> bool:
        result = next(iter(self._expectation.actual), ...)

        return result is ...
