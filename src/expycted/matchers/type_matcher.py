from expycted.core.matchers import BaseMatcher


class TypeMatcher(BaseMatcher):
    """Assert that the actual type is equivalent to the expected type."""

    OPERATION = "type"

    def _matches(self, expected, **kwargs) -> bool:
        return type(self._actual) is expected
