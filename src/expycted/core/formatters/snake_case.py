from .base_formatter import BaseFormatter

import re

class SnakeCase(BaseFormatter):
    PATTERN = re.compile(r"(?<!^)(?=[A-Z])")

    def __str__(self) -> str:
        """Convert *CamelCase* strings to *snake_case*."""

        return self.PATTERN.sub("_", self._value).lower()
