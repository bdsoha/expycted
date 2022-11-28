from typing import Callable, Any

from expycted.internals.filesystem import Directory
from expycted.internals.function import Function
from expycted.internals.value import To, ToNot


class expect:
    def __init__(self, value: Any):
        """Expect a value to be something

        Args:
            value (Any): Value to check for some sort of condition
        """
        self.value = value

    @property
    def to(self):
        return To(self.value)

    @property
    def to_not(self):
        return ToNot(self.value)

    @staticmethod
    def function(function: Callable):
        """Expect a function to do something

        Args:
            function (callable): Function to check for some sort of condition
        """
        return Function(function)

    @staticmethod
    def value(value: Any):
        """Expect a value to be something

        Args:
            value (Any): Value to check for some sort of condition
        """
        return expect(value)

    @staticmethod
    def folder(path: str):
        """Expect a folder to be something

        Args:
            path (str): Path to folder to check for some sort of condition
        """
        return Directory(path)

    directory = folder
