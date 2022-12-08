from enum import Enum
from typing import Any, Optional
from . import SENTINEL


class ValueFormatter:
    """Format values to indicate their type when output to the console."""

    _LOOKUP = [
        "str",
        "byte",
        "enum",
        "builtin",
        "callable"
    ]

    @classmethod
    def _fqn(cls, source):
        return f"{source.__module__}.{source.__name__}"

    def __init__(self, value):
        self._value = value

    @classmethod
    def _to_byte(cls, value):
        if isinstance(value, bytes):
            return f"b\"{value.decode()}\""

        return None

    @classmethod
    def _to_str(cls, value):
        if isinstance(value, str):
            return f"\"{value}\""

        return None

    @classmethod
    def _to_enum(cls, value):
        if isinstance(value, Enum):
            return f"{cls._fqn(value.__class__)}.{value.name}"

        return None

    @classmethod
    def _to_builtin(cls, value):
        if value.__class__.__module__ not in ('builtins', 'enum'):
            return f"{cls._fqn(value.__class__)}@{hex(id(value))}"

        return None

    @classmethod
    def _to_callable(cls, value):
        if callable(value):
            return cls._fqn(value)

        return None

    @classmethod
    def _to(cls, name, value):
        return getattr(cls, f"_to_{name}")(value)

    @classmethod
    def format(cls, value) -> str:
        """Facade to guess the correct formatter based on the value type."""

        if value is SENTINEL:
            return ""

        instance = cls(value)

        return next(
            filter(None, (instance._to(name, value) for name in cls._LOOKUP)),
            str(value)
        )


class Message:
    """Generate assertion output message."""

    def __init__(
        self,
        method: str,
        *,
        operation: Optional[str] = None,
        negated: bool = False
    ):
        self._method = method
        self._operation = operation
        self._negated = negated

    def _format_value(self, value: Any) -> str:
        return ValueFormatter.format(value)

    def lead(self, *, actual: Any, expected: Any = SENTINEL) -> str:
        """The expectation *as code* that was executed."""

        return "".join([
            f"expect({self._format_value(actual)})",
            ".to_not" if self._negated else ".to",
            f".{self._method}({self._format_value(expected)})",
            f" # Using `{self._operation}`" if self._operation else ""
        ])
