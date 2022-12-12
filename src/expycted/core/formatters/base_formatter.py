from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    """Abstract class to handle construction and facade."""

    def __init__(self, value):
        self._value = value

    @abstractmethod
    def __str__(self) -> str:
        ...

    @classmethod
    def format(cls, value) -> str:
        """Facade for ``str()``."""

        return str(cls(value))
