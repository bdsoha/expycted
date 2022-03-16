from typing import Any

class Function:
    def __init__(self, function: callable):
        self.function = function

    def to_raise(self, exception: Exception = Exception):
        """Check if the function raises the exception

        Args:
            exception (Exception): Exception to expect
        """
        return ToRaise(exception=exception, function=self.function)

    def to_return(self, value: Any = None, type_of_value: type = None):
        """ Check if the function returns provided value or type

        Args:
            value (Any, optional): Value that is expected to be returned. Defaults to None.
            type_of_value (type, optional): Type of value that is expected to be returned. Defaults to None.

        Raises:
            AssertionError: When neither of type_of_value and value is not provided AssertionError is raised
        """
        if value is None and type_of_value is None:
            raise AssertionError(
                'You must specify either value or type_of_value in to_return function')
        else:
            return ToReturn(value=value, type_of_value=type_of_value, function=self.function)


class ToRaise:
    function: callable
    exception: Exception

    def __init__(self, exception: Exception, function: callable):
        self.function = function
        self.exception = exception

    def when_called_with(self, *args, **kwargs):
        """Arguments to call the function with

        Raises:
            AssertionError: When function doesn't raise the expected exception AssertionError is raised
        """
        try:
            self.function(*args, **kwargs)
        except Exception as e:
            assert issubclass(type(e), self.exception)
        else:
            raise AssertionError(
                f"Expected '{self.exception}' to be raised, but nothing was raised")

    when_called_with_args = when_called_with_arguments = when_called_with


class ToReturn:
    function: callable
    value: Any
    type_of_value: type

    def __init__(self, function: callable, value, type_of_value):
        self.function = function
        self.value = value
        self.type_of_value = type_of_value

    def when_called_with(self, *args, **kwargs):
        """Arguments to call the function with

        Raises:
            AssertionError: When function value or type_of_value is not matched AssertionError is raised
        """
        ret = self.function(*args, **kwargs)
        if self.value is not None:
            assert ret == self.value
        if self.type_of_value is not None:
            assert type(ret) == self.type_of_value

    when_called_with_args = when_called_with_arguments = when_called_with