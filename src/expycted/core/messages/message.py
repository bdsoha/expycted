from typing import Any, Optional, Tuple, Union
from expycted.core.formatters import ValueToString
from expycted.core.utilities import SENTINEL
from .detail_message import DetailMessage


class Message:
    """Generate assertion output message."""

    def __init__(
        self,
        method: str,
        *,
        operation: Optional[str] = None,
        negated: bool = False,
        message: Optional[Union[DetailMessage, str]] = None
    ):
        self._method = method
        self._operation = operation
        self._negated = negated
        self._message = message

    @staticmethod
    def _format_values(*values: str) -> Tuple[str, str]:
        return tuple(map(ValueToString, values))

    @property
    def _to(self) -> str:
        return "to_not" if self._negated else "to"

    def signature(self, *, actual: Any, expected: Any = SENTINEL) -> str:
        """Expectation method signature *(as code)* that was executed."""

        actual, expected = self._format_values(actual, expected)

        return "".join([
            f"expect({actual})",
            ".",
            self._to,
            ".",
            f"{self._method}({expected})",
            f" # Using `{self._operation}`" if self._operation else ""
        ])

    def details(self, *, actual: Any, expected: Any = SENTINEL) -> str:
        """Detail difference between the ``actual`` and ``expected`` values."""

        actual, expected = self._format_values(actual, expected)

        placeholders = dict(
            to=self._to.replace("_", " "),
            expected=expected,
            actual=actual,
            method=self._method,
            method_split=self._method.replace("_", " ")
        )

        message = DetailMessage() if not self._message else self._message

        if isinstance(message, str):
            return message.format(**placeholders)

        return "\n".join([
            message.expected.format(**placeholders),
            message.actual.format(**placeholders),
        ])

    def render(self, actual: Any, expected: Any = SENTINEL) -> str:
        return "\n\n".join([
            self.signature(actual=actual, expected=expected),
            self.details(actual=actual, expected=expected)
        ])
