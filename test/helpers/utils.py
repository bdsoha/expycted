from contextlib import nullcontext
from typing import NamedTuple

import pytest


class Context(NamedTuple):
    not_raises = nullcontext()
    raises = pytest.raises(AssertionError)


CONTEXT = Context()


def expected_params(params, argnames="expected", extract_ids=True, **kwargs):
    if extract_ids:
        kwargs['ids'] = tuple(map(lambda i: i[-1], params))
        params = tuple(map(lambda i: i[:-1], params))

    return pytest.mark.parametrize(argnames, argvalues=params, **kwargs)


def expected_actual_params(params, argnames="expected,actual", **kwargs):
    return expected_params(params, argnames, **kwargs)
