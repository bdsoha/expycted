from typing import Any

from expycted.core.matchers import BaseMatcher


class EqualMatcher(BaseMatcher):
    """Asserts that two variables have the same value."""

    OPERATION = "=="

    def _matches(self, *, expected: Any, **kwargs) -> bool:
        return self._actual == expected
