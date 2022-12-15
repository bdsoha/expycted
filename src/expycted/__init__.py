from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Union

from expycted.internals.filesystem import Directory
from expycted.internals.function import Function
from expycted.internals.value import Value

__version__ = "0.8.2"


class _Expect(Value):
    @classmethod
    def function(cls, function: Callable):
        """Expect a function to do something

        Args:
            function (callable): Function to check for some sort of condition
        """
        return Function(function)

    @classmethod
    def value(cls, expected: Any):
        """Expect a value to be something

        Args:
            expected (Any): Value to check for some sort of condition
        """
        return cls(expected)

    @classmethod
    def folder(cls, path: Union[str, Path]):
        """Expect a folder to be something

        Args:
            path (str|Path): Path to folder to check for some sort of condition
        """
        return Directory(path)

    directory = folder


expect = _Expect
