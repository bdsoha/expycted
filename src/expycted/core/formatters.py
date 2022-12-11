from enum import Enum
from .utilities import SENTINEL


class StringOutputFormatter:
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

        return next(
            filter(None, (cls._to(name, value) for name in cls._LOOKUP)),
            str(value)
        )
