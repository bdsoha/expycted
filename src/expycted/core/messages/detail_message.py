from __future__ import annotations

from typing import NamedTuple


class DetailMessage(NamedTuple):
    actual: str = "Actual\t: {actual}"
    expected: str = "Expected\t: {expected}"
