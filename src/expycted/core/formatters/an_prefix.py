from __future__ import annotations

from .base_formatter import BaseFormatter


class AnPrefix(BaseFormatter):
    """Return ``"a"`` or ``"an"`` based on subsequent vowel."""

    VOWELS = ("a", "e", "i", "o", "u")

    def __str__(self) -> str:
        found = next(filter(str.isalpha, str(self._value)))

        return "an" if found.lower() in self.VOWELS else "a"
