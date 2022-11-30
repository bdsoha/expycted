import pytest
from contextlib import nullcontext

DOES_NOT_RAISE = nullcontext()
RAISES_ASSERTION = pytest.raises(AssertionError)
