from __future__ import annotations

from typing import Any

from expycted.core.decorators import chain
from expycted.internals.utils import hidetraceback


class BaseExpectation:
    _ASSERTION_MESSAGES = {}

    def __init__(self, expected: Any, negate=False):
        self.expected = expected
        self.negate = negate

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
        if self.negate:
            result = not result
            message = message.replace(" to ", " to not ")

        assert result, message

        self.negate = False

        return self

    @hidetraceback
    def _execute_internal_assertion(self, method: str, *args, **kwargs):
        internal_assert = getattr(self, f"_internal_{method}")

        return self._assert(*internal_assert(*args, **kwargs))

    @property
    @chain
    def to(self):
        self.negate = False

    @property
    def and_to(self):
        return self.to

    @property
    @chain
    def to_not(self):
        self.negate = True

    @property
    def and_to_not(self):
        return self.to_not

    @property
    def and_not(self):
        return self.to_not
