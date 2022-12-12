from expycted.core.matchers import BaseMatcher


class IsMatcher(BaseMatcher):
    """Asserts that the actual value is the expected value."""

    OPERATION = "is"

    def __init__(self, *args, to_match, **kwargs):
        super().__init__(*args, **kwargs)
        self._to_match = to_match

    def _matches(self, **kwargs) -> bool:
        return self._actual is self._to_match
