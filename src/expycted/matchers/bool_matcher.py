from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple

from .constant_matcher import ConstantMatcher


class BoolMatcher(ConstantMatcher, ABC):
    """Base class for boolean assertions."""

    @abstractmethod
    def _str_equivalent(self) -> Tuple[str, ...]:
        ...

    def _matches(self, expected) -> bool:
        # if self._qualifiers.from_str:
        # return str(self._expectation.actual).lower() in self._str_equivalent()

        if self._expectation.is_strict:
            return super()._matches(expected)

        return bool(self._expectation.actual) is self._to_match
