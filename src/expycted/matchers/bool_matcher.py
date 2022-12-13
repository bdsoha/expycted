from expycted.core.matchers import BaseMatcher


class BoolMatcher(BaseMatcher):
    """Asserts that the actual value is boolean equivalent to the expected value."""

    OPERATION = "bool"

    def _matches(self, **kwargs) -> bool:
        return bool(self._actual) is self._to_match
