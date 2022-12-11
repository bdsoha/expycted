from typing import Type


class MatcherError(TypeError):
    """Matcher cannot handle the provided type."""

    def __init__(self, actual: Type, *allowed: Type):
        super().__init__()
        self._actual = actual
        self._allowed = allowed

    @staticmethod
    def _a_or_an(value) -> str:
        return "an" if value in ["a", "e", "i", "o", "u"] else "a"

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

        return "\n".join([
            "Matcher Error:",
            f"Received value must be {self._a_or_an(allowed[1])} {allowed}.",
            f"But, {self._a_or_an(self._actual)} `{self._actual.__name__}` was provided."
        ])
