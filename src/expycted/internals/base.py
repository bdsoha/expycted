from __future__ import annotations

from typing import Any
from warnings import warn

from expycted.core.expectations import Expectation
from expycted.internals.utils import hidetraceback


class BaseExpectation(Expectation):
    _ASSERTION_MESSAGES: Any = {}

    @property
    def expected(self):
        warn("Swap `expected` with `actual`", DeprecationWarning, stacklevel=2)
        return self.actual

    def _message(
        self,
        method: str,
        actual: Any = ...,
        expected: Any = None,
        **kwargs,
    ) -> str:
        placeholders = dict(
            expected=self.expected if expected is None else expected,
            **kwargs,
        )

        if actual is not ...:
            placeholders["actual"] = actual

        return self._ASSERTION_MESSAGES[method].format(**placeholders)

    @hidetraceback
    def _assert(self, result: bool, message: str):
        if self.qualifiers.negated:
            result = not result
            message = message.replace(" to ", " to not ")

        assert result, message

        return self  # .clear()

    @hidetraceback
    def _execute_internal_assertion(self, method: str, *args, **kwargs):
        internal_assert = getattr(self, f"_internal_{method}")

        return self._assert(*internal_assert(*args, **kwargs))
