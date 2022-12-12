from typing import Type

from expycted.core.formatters import AnPrefix


class MatcherError(TypeError):
    """Matcher cannot handle the provided type."""

    def __init__(self, actual: Type, *allowed: Type):
        super().__init__()
        self._actual = actual
        self._allowed = allowed

    def __str__(self) -> str:
        allowed = sorted(map(lambda t: f"`{t.__name__}`", self._allowed))

        size = len(allowed)

        if size == 1:
            allowed = allowed[0]

        if size == 2:
            allowed = " or ".join(allowed)

        if size > 2:
            last = allowed.pop()
            allowed = ", ".join(allowed)
            allowed += f", or {last}"

        return "\n".join(
            [
                "Matcher Error:",
                f"Received value must be {AnPrefix(allowed)} {allowed}.",
                f"But, {AnPrefix(self._actual)} `{self._actual.__name__}` was provided.",
            ]
        )
