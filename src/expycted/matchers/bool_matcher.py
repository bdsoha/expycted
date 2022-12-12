from expycted.core.matchers import BaseMatcher


class BoolMatcher(BaseMatcher):
    """Asserts that the actual value is boolean equivelent to the expected value."""

    OPERATION = "bool"

    def __init__(self, actual, *, to_match, **kwargs):
        super().__init__(actual, **kwargs)
        self._to_match = to_match

    def _matches(self, **kwargs) -> bool:
        return bool(self._actual) is self._to_match
