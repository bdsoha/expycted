from pathlib import Path
from typing import Callable, Any, Union

from expycted.internals.filesystem import Directory
from expycted.internals.function import Function
from expycted.internals.value import Value


class expect(Value):
    @classmethod
    def function(cls, function: Callable):
        """Expect a function to do something

        Args:
            function (callable): Function to check for some sort of condition
        """
        return Function(function)

    @classmethod
    def value(cls, value: Any):
        """Expect a value to be something

        Args:
            value (Any): Value to check for some sort of condition
        """
        return cls(value)

    @classmethod
    def folder(cls, path: Union[str, Path]):
        """Expect a folder to be something

        Args:
            path (str|Path): Path to folder to check for some sort of condition
        """
        return Directory(path)

    directory = folder
