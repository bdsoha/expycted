from __future__ import annotations

from enum import Enum

from .base_formatter import BaseFormatter


class ValueToString(BaseFormatter):
    """Convert to the correct formatting based on the value type."""

    _LOOKUP = [
        "str",
        "byte",
        "enum",
        "builtin",
        "callable",
    ]

    @classmethod
    def _fqn(cls, source):
        return f"{source.__module__}.{source.__name__}"

    def _to_byte(self):
        if isinstance(self._value, bytes):
            return f'b"{self._value.decode()}"'

        return None

    def _to_str(self):
        if isinstance(self._value, str):
            return f'"{self._value}"'

        return None

    def _to_enum(self):
        if isinstance(self._value, Enum):
            return f"{self._fqn(self._value.__class__)}.{self._value.name}"

        return None

    def _to_builtin(self):
        if self._value.__class__.__module__ not in ("builtins", "enum"):
            return f"{self._fqn(self._value.__class__)}@{hex(id(self._value))}"

        return None

    def _to_callable(self):
        if callable(self._value):
            return self._fqn(self._value)

        return None

    def _to(self, name):
        return getattr(self, f"_to_{name}")()

    def __str__(self) -> str:
        """Convert to the correct formatting based on the value type."""

        if self._value is ...:
            return ""

        return next(
            filter(None, map(self._to, self._LOOKUP)),
            str(self._value),
        )
