from typing import Any

from expycted.internals.utils import hidetraceback

_SENTINEL = object()


class BaseExpectation:
    _ASSERTION_MESSAGES = {}

    def __init__(self, expected: Any, negate=False):
        self.expected = expected
        self.negate = negate

    def _message(
            self,
            method: str,
            actual: Any = _SENTINEL,
            expected: Any = None,
            **kwargs
    ) -> str:
        placeholders = dict(
            expected=self.expected if expected is None else expected,
            **kwargs
        )

        if actual is not _SENTINEL:
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

        return self._assert(
            *internal_assert(*args, **kwargs)
        )

    @property
    def to(self):
        self.negate = False
        return self

    @property
    def and_to(self):
        return self.to

    @property
    def to_not(self):
        self.negate = True
        return self

    @property
    def and_to_not(self):
        return self.to_not

    @property
    def and_not(self):
        return self.to_not
