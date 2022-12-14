from .bool_matcher import BoolMatcher


class IsTrueMatcher(BoolMatcher):
    """Asserts that the actual value is ``True``."""

    OPERATION = "is True"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, to_match=True, **kwargs)

    @property
    def _str_equivalent(self):
        return ("true", "1")
