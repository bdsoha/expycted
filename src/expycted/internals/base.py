from typing import Any

_SENTIAL = object()


class BaseExpectation:
    _ASSERTION_MESSAGES = {}

    def __init__(self, value: Any, negate=False):
        self.value = value
        self.negate = negate

    def _message(self, method: str, actual: Any = _SENTIAL) -> str:
        placeholders = dict(value1=self.value)

        if actual is not _SENTIAL:
            placeholders['value2'] = actual

        return self._ASSERTION_MESSAGES[method].format(**placeholders)

    def _execute_internal_assertion(self, method: str, *args, **kwargs):
        internal_assert = getattr(self, f"_internal_{method}")
        res, message = internal_assert(*args, **kwargs)

        if self.negate:
            res = not res
            message = message.replace(" to ", " to not ")

        assert res, message

    @property
    def to(self):
        return self

    @property
    def and_to(self):
        return self.to

    @property
    def to_not(self):
        self.negate = not self.negate
        return self

    @property
    def and_to_not(self):
        return self.to_not

    @property
    def and_not(self):
        return self.to_not
