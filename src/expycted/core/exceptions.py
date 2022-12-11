from typing import Type


class MatcherError(TypeError):
    """Matcher cannot handle the provided type."""

    def __init__(self, *allowed: Type):
        super().__init__()
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

        a_or_an = "an" if allowed[1] in ["a", "e", "i", "o", "u"] else "a"

        return f"Matcher Error: recieved value must be {a_or_an} {allowed}"
