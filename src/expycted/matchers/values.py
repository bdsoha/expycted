from typing import Any, Iterable
from expycted.core.matchers import BaseMatcher
from expycted.core.utilities import SENTINEL


class EqualMatcher(BaseMatcher):
    """Asserts that two variables have the same value."""

    OPERATION = "=="

    def _matches(self, *, expected: Any, **kwargs) -> bool:
        return self._actual == expected


class BeEmptyMatcher(BaseMatcher):
    """Asserts that the value is empty."""

    ALLOWED_TYPES = (Iterable,)
    MESSAGE = "Expected {actual} {to} be empty, but it was not."

    def _matches(self, **kwargs) -> bool:
        result = next(iter(self._actual), SENTINEL)

        return result is SENTINEL
