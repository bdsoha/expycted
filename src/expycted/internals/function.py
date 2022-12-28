from __future__ import annotations

from typing import Any, Callable, Optional, Type

from expycted.internals.base import BaseExpectation
from expycted.internals.utils import hidetraceback


class Function:
    def __init__(self, actual: Callable):
        self.actual = actual

    def to_raise(self, exception: Optional[Type[Exception]] = None):
        """Check if the function raises the exception

        Args:
            exception (Exception): Exception to expect
        """
        return ToRaise(
            actual=self.actual,
            exception=exception if exception else Exception,
        )

    def to_return(self, value: Any = None, type_of_value: Optional[Type] = None):
        """Check if the function returns provided value or type

        Args:
            value: Value that is expected to be returned. Defaults to None.
            type_of_value: Type of the expected return value. Defaults to None.

        Raises:
            AssertionError: When neither of type_of_value and value is not provided AssertionError is raised
        """
        if value is None and type_of_value is None:
            raise ValueError(
                "You must specify either value or type_of_value in to_return function"
            )

        return ToReturn(
            self.actual,
            value=value,
            type_of_value=type_of_value,
        )


def format_args_kwargs(args: Any, kwargs: Any) -> str:
    """Format arguments and keyword arguments to string

    Args:
        args (Any): Arguments
        kwargs (Any): Keyword arguments

    Returns:
        str: Formatted arguments and keyword arguments
    """
    args_str = ", ".join(map(str, args))
    kwargs_str = ", ".join(map(lambda x: f"{x[0]}={x[1]}", kwargs.items()))

    return f"\n\t- arguments: {args_str} \n\t- keyword arguments: {kwargs_str}"


class ToRaise(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "to_raise": "Expected function `{expected}` to raise {actual} when called with: {arguments}",
    }

    def __init__(self, actual: Callable, *, exception: Type[Exception], **kwargs):
        super().__init__(actual, **kwargs)
        self.exception = exception

    @hidetraceback
    def when_called_with(self, *args, **kwargs):
        """Arguments to call the function with

        Raises:
            AssertionError: When function doesn't raise the expected exception AssertionError is raised
        """
        try:
            self.expected(*args, **kwargs)
        except Exception as e:
            self._assert(
                issubclass(type(e), self.exception),
                self._message(
                    "to_raise",
                    self.exception,
                    expected=self.expected.__name__,
                    arguments=format_args_kwargs(args, kwargs),
                ),
            )
        else:
            raise AssertionError(
                f"Expected '{self.exception}' to be raised, but nothing was raised"
            )

    when_called_with_args = when_called_with_arguments = when_called_with


class ToReturn(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "to_return": "Expected function {expected} to return {actual} when called with: {arguments}",
        "to_return_type": "Expected value ({actual}) returned by function {expected} to be of type {type} when called with: {arguments}",
    }

    def __init__(self, actual: Callable, value, type_of_value, **kwargs):
        super().__init__(actual, **kwargs)
        self.value = value
        self.type_of_value = type_of_value

    @hidetraceback
    def when_called_with(self, *args, **kwargs):
        """Arguments to call the function with

        Raises:
            AssertionError: When function value or type_of_value is not matched AssertionError is raised
        """
        ret = self.expected(*args, **kwargs)

        substitutions = dict(
            actual=self.value,
            expected=self.expected.__name__,
            arguments=format_args_kwargs(args, kwargs),
        )

        if self.value is not None:
            self._assert(ret == self.value, self._message("to_return", **substitutions))

        if self.type_of_value is not None:
            self._assert(
                type(ret) == self.type_of_value,
                self._message("to_return", type=self.type_of_value, **substitutions),
            )

    when_called_with_args = when_called_with_arguments = when_called_with
