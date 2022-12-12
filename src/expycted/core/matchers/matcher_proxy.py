from typing import Type
from .base_matcher import BaseMatcher
from expycted.core.utilities import SENTINEL
from typing import Any


def factory(base: Type[BaseMatcher]):
    class _(base):
        def __call__(self, expected: Any = SENTINEL, **kwargs):
            results = super().__call__(expected=expected, **kwargs)

            assert results, self.message().render(self._actual, expected=expected)

    return _
