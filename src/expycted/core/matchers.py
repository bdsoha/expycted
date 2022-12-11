from abc import ABC, abstractmethod
from typing import Any, Callable, Optional, Union
from .messages import DetailMessage


class BaseMatcher(ABC):
    MESSAGE: Optional[Union[str, DetailMessage]]

    def __init__(self, *, expectation):
        self._expectation = expectation

    @property
    def _should_negate(self) -> bool:
        return self._expectation.negated

    @abstractmethod
    def _matches(self, **kwargs) -> bool:
        ...

    def _negate(self, **kwargs) -> bool:
        return not self._matches(**kwargs)

    def _get_match_method(self, **kwargs) -> Callable:
        method_name = "_negate" if self._should_negate else "_matches"

        return getattr(self, method_name)

    def __call__(self, **kwargs) -> bool:
        method = self._get_match_method(**kwargs)

        try:
            return method(**kwargs)
        except TypeError as error:
            return self._handle_type_error(error, **kwargs)


class BaseBinaryMatcher(BaseMatcher):
    @abstractmethod
    def _matches(self, *, expected: Any, **kwargs) -> bool:
        ...

    def _negate(self, *, expected: Any, **kwargs) -> bool:
        return super()._negate(expected=expected, **kwargs)
    