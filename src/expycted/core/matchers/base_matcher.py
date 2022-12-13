from abc import ABC, abstractmethod
from copy import copy
from typing import Any, Optional, Tuple, Type, Union
import re

from expycted.core.exceptions import MatcherError
from expycted.core.formatters import SnakeCase
from expycted.core.messages import DetailMessage, Message

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

TAllowedTypes = Union[Literal["*"], Tuple[Type, ...]]


class BaseMatcher(ABC):
    OPERATION: Optional[str] = None
    MESSAGE: Optional[Union[str, DetailMessage]] = None
    ALLOWED_TYPES: TAllowedTypes = "*"

    def __init__(
        self,
        actual: Any,
        *,
        negated: bool = False,
        alias: str = None,
        to_match: Any = None
    ):
        self._actual = actual
        self._alias = alias
        self._negated = negated
        self._to_match = to_match

    @abstractmethod
    def _matches(self, *, expected: Any, **kwargs) -> bool:
        ...

    def _negate(self, *, expected: Any, **kwargs) -> bool:
        return not self._matches(expected=expected, **kwargs)

    def _get_message(self, **kwargs):
        return self.MESSAGE

    def _get_operation(self, **kwargs):
        return self.OPERATION

    def _validate_allowed_types(self, **kwargs):
        allowed_types = self.allowed_types(**kwargs)

        if allowed_types == "*":
            return

        if not isinstance(self._actual, allowed_types):
            raise MatcherError(*allowed_types, actual=type(self._actual))

    def allowed_types(self, **kwargs) -> TAllowedTypes:
        """Types that are allowed to be compared."""

        return copy(self.ALLOWED_TYPES)

    def name(self, **kwargs) -> str:
        """Simplified name for the matcher based on the class name."""

        if self._alias:
            return self._alias

        name = re.sub("Matcher$", "", self.__class__.__name__)

        return SnakeCase.format(name)

    def message(self, **kwargs) -> Message:
        """Build the assertion message."""

        return Message(
            method=self.name(**kwargs),
            negated=self._negated,
            operation=self._get_operation(**kwargs),
            message=self._get_message(**kwargs),
            **kwargs,
        )

    def __call__(self, expected: Any = ..., **kwargs) -> bool:
        self._validate_allowed_types(**kwargs)

        method_name = "_negate" if self._negated else "_matches"

        method = getattr(self, method_name)

        return method(expected=expected, **kwargs)
