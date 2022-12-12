from typing import Any, Type

from .base_matcher import BaseMatcher


def factory(base: Type[BaseMatcher]):
    class _(base):
        def __call__(self, expected: Any = ..., **kwargs):
            results = super().__call__(expected=expected, **kwargs)

            assert results, self.message().render(self._actual, expected=expected)

    return _
