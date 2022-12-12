from typing import Any, NamedTuple


class DetailMessage(NamedTuple):
    actual: str = "Actual\t: {actual}"
    expected: str = "Expected\t: {expected}"
