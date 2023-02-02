from __future__ import annotations

from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params


@expected_actual_params(stubs.NOT_CONTAIN)
def test_to_not_contain(expected, actual, context):
    expect(expected).to_not.contain(actual)

    with context.raises:
        expect(expected).to.contain(actual)
