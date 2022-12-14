from __future__ import annotations

from .bool_matcher import BoolMatcher


class IsFalseMatcher(BoolMatcher):
    """Asserts that the actual value is ``False``."""

    OPERATION = "is False"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, to_match=False, **kwargs)

    @property
    def _str_equivalent(self):
        return ("false", "0")
