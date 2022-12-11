from abc import ABC, abstractmethod
from copy import copy
from typing import Any, Optional, Tuple, Type, Union
from .messages import DetailMessage, Message
from .utilities import SENTINEL
from .exceptions import MatcherError

import re

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


TAllowedTypes = Union[Literal["*"], Tuple[Type, ...]]


class BaseMatcher(ABC):
    OPERATION: Optional[str] = None
    MESSAGE: Optional[Union[str, DetailMessage]] = None
    ALLOWED_TYPES = TAllowedTypes = "*"

    def __init__(
        self,
        actual: Any,
        *,
        negated: bool = False,
        alias: str = None,
        safe=False
    ):
        self.alias = alias
        self._actual = actual
        self._negated = negated
        self._safe = safe

    @abstractmethod
    def _matches(self, *, expected: Any, **kwargs) -> bool:
        ...

    def _negate(self, *, expected: Any, **kwargs) -> bool:
        return not self._matches(expected=expected, **kwargs)

    def _get_message(self, **kwargs):
        return self.MESSAGE

    def _validate_allowed_types(self, **kwargs):
        allowed_types = self.allowed_types(**kwargs)

        if allowed_types == "*":
            return

        if not isinstance(self._actual, allowed_types):
            raise MatcherError(*allowed_types)

    def allowed_types(self, **kwargs) -> TAllowedTypes:
        """Types that are allowed to be compared."""

        return copy(self.ALLOWED_TYPES)

    def name(self, **kwargs) -> str:
        """Simplifed name for the matcher based on the class name."""

        if self.alias:
            return self.alias

        name = self.__class__.__name__

        name = re.sub("Matcher$", "", name)

        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    def message(self, **kwargs) -> Message:
        """Build the assertion message."""

        return Message(
            method=self.name(**kwargs),
            negated=self._negated,
            operation=self.OPERATION,
            message=self._get_message(**kwargs),
            **kwargs
        )

    def __call__(self, expected: Any = SENTINEL, **kwargs) -> bool:
        self._validate_allowed_types(**kwargs)

        method_name = "_negate" if self._negated else "_matches"

        method = getattr(self, method_name)

        results = method(expected=expected, **kwargs)

        if self._safe:
            return results

        assert results, self.message().render(self._actual, expected=expected)

    @classmethod
    def safe(cls, actual: Any, **kwargs):
        """Do not raise ``AssertionErrors``."""

        return cls(actual, safe=True, **kwargs)
