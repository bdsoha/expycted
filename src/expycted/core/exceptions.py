from __future__ import annotations

from typing import Type

from expycted.core.formatters import AnPrefix


class MatcherError(TypeError):
    """Matcher cannot handle the provided type."""

    def __init__(self, *allowed: Type, actual: Type):
        super().__init__()
        self._actual = actual
        self._allowed = allowed

    def __str__(self) -> str:
        allowed = sorted(map(lambda t: f"`{t.__name__}`", self._allowed))
        output = ""
        an = AnPrefix(self._actual)

        size = len(allowed)

        if size == 1:
            output = allowed[0]

        if size == 2:
            output = " or ".join(allowed)

        if size > 2:
            last = allowed.pop()
            output = ", ".join(allowed)
            output += f", or {last}"

        return "\n".join(
            [
                "Matcher Error:",
                f"Received value must be {AnPrefix(output)} {output}.",
                f"But, {an} `{self._actual.__name__}` was provided.",
            ]
        )
