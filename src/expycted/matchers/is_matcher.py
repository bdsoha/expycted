from expycted.core.matchers import BaseMatcher


class IsMatcher(BaseMatcher):
    """Asserts that the actual value is the expected value."""

    OPERATION = "is"

    def _matches(self, expected) -> bool:
        return self._actual is self._to_match
