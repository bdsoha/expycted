from __future__ import annotations

import re

from .base_formatter import BaseFormatter


class SnakeCase(BaseFormatter):
    """Convert *CamelCase* strings to *snake_case*."""

    PATTERN = re.compile(r"(?<!^)(?=[A-Z])")

    def __str__(self) -> str:

        return self.PATTERN.sub("_", self._value).lower()
