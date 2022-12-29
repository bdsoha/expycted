from __future__ import annotations

from abc import ABC, abstractmethod
from copy import copy
from typing import Any, Optional, Tuple, Type, Union
import re
import sys

from expycted.core.exceptions import MatcherError
from expycted.core.expectations.expectation import Expectation
from expycted.core.formatters import SnakeCase
from expycted.core.messages import DetailMessage, Message

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

TAllowedTypes = Union[Literal["*"], Tuple[Type, ...]]


class BaseMatcher(ABC):
    OPERATION: Optional[str] = None
    MESSAGE: Optional[Union[str, DetailMessage]] = None
    ALLOWED_TYPES: TAllowedTypes = "*"

    def __init__(
        self,
        expectation: Any,
        *,
        alias: Optional[str] = None,
        to_match: Any = None,
        **kwargs,
    ):
        self._expectation = Expectation.get_or_create(expectation, **kwargs)
        self._alias = alias
        self._to_match = to_match

    @abstractmethod
    def _matches(self, *, expected: Any) -> bool:
        ...

    def _negate(self, *, expected: Any) -> bool:
        return not self._matches(expected=expected)

    def _get_message(self):
        return self.MESSAGE

    def _get_operation(self):
        return self.OPERATION

    def _validate_allowed_types(self):
        allowed_types = self.allowed_types()

        if allowed_types == "*":
            return

        if isinstance(self._expectation.actual, allowed_types):
            return

        raise MatcherError(*allowed_types, actual=type(self._expectation.actual))

    def allowed_types(self) -> TAllowedTypes:
        """Types that are allowed to be compared."""

        return copy(self.ALLOWED_TYPES)

    def name(self) -> str:
        """Simplified name for the matcher based on the class name."""

        if self._alias:
            return self._alias

        name = re.sub("Matcher$", "", self.__class__.__name__)

        return SnakeCase.format(name)

    def message(self) -> Message:
        """Build the assertion message."""

        return Message(
            method=self.name(),
            negated=self._expectation.is_negated,
            operation=self._get_operation(),
            message=self._get_message(),
        )

    def __call__(self, expected: Any = ...) -> bool:
        self._validate_allowed_types()

        method_name = "_negate" if self._expectation.is_negated else "_matches"

        method = getattr(self, method_name)

        results = method(expected=expected)

        return results

    def __eq__(self, other: Any) -> bool:
        """Compare two matcher instances."""

        if not isinstance(other, self.__class__):
            return False

        return all(
            [
                # @TODO: check qualifiers
                type(self) is type(other),
                self._expectation.is_negated is other._expectation.is_negated,
                self._expectation.actual == other._expectation.actual,
                self._to_match == other._to_match,
            ]
        )
