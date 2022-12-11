from abc import ABC, abstractmethod
from typing import Any, Literal, Optional, Tuple, Type, Union
from .messages import DetailMessage
from .utilities import SENTINEL
from .exceptions import MatcherError

TAllowedTypes = Union[Literal["*"], Tuple[Type, ...]]


class BaseMatcher(ABC):
    MESSAGE: Optional[Union[str, DetailMessage]]
    ALLOWED_TYPES = TAllowedTypes = "*"

    def __init__(self, actual: Any, *, negated: bool = False):
        self._actual = actual
        self._negated = negated

    @abstractmethod
    def _matches(self, *, expected: Any, **kwargs) -> bool:
        ...

    def _negate(self, *, expected: Any, **kwargs) -> bool:
        return not self._matches(expected=expected, **kwargs)

    def _get_allowed_types(self, **kwargs) -> TAllowedTypes:
        return self.ALLOWED_TYPES

    def _validate_allowed_types(self, **kwargs):
        allowed_types = self._get_allowed_types(**kwargs)

        if allowed_types == "*":
            return

        if not isinstance(self._actual, allowed_types):
            raise MatcherError(*allowed_types)

    def __call__(self, *, expected: Any = SENTINEL, **kwargs) -> bool:
        self._validate_allowed_types(**kwargs)

        method_name = "_negate" if self._negated else "_matches"

        method = getattr(self, method_name)

        return method(expected=expected, **kwargs)
