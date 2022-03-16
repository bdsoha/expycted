from expycted.internals import (
    To,
    ToNot
)

from expycted.internals.function import Function

class expect:
    def __init__(self, value: any):
        """Expect a value to be something

        Args:
            value (any): Value to check for some sort of condition
        """
        self.to = To(value)
        self.to_not = ToNot(value)

    @staticmethod
    def function(function: callable):
        """Expect a function to do something

        Args:
            function (callable): Function to check for some sort of condition
        """
        return Function(function)

    @staticmethod
    def value(value: any):
        """Expect a value to be something

        Args:
            value (any): Value to check for some sort of condition
        """
        return expect(value)
