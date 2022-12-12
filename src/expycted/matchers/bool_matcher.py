from .is_matcher import IsMatcher


class BoolMatcher(IsMatcher):
    """Asserts that the actual value is boolean equivalent to the expected value."""

    OPERATION = "bool"

    @property
    def _normalized_actual(self):
        return bool(self._actual)
