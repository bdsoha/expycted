from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple

from expycted.core.decorators import chain

from .is_matcher import IsMatcher


class BoolMatcher(IsMatcher, ABC):
    """Base class for boolean assertions"""

    @property
    @chain
    def from_str(self):
        self._qualifiers.from_str = True

    @property
    @chain
    def weak(self):
        self._qualifiers.weak = True

    @abstractmethod
    def _str_equivalent(self) -> Tuple[str, ...]:
        ...

    def _matches(self, expected) -> bool:
        if self._qualifiers.from_str:
            return str(self._actual).lower() in self._str_equivalent()

        if self._qualifiers.weak:
            return bool(self._actual) is self._to_match

        return super()._matches(expected)
