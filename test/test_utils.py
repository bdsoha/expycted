import pytest
from contextlib import nullcontext


DOES_NOT_RAISE = nullcontext()
RAISES_ASSERTION = pytest.raises(AssertionError)


def expected_params(params, argnames="expected,context", **kwargs):
    return pytest.mark.parametrize(argnames, argvalues=params, **kwargs)

def expected_actual_params(params, argnames="expected,actual,context", **kwargs):
    return expected_params(params, argnames, **kwargs)
