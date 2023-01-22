from __future__ import annotations

from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params


@expected_actual_params(stubs.CONTAIN)
def test_to_contain(expected, actual, context):
    expect(expected).to.contain(actual)
    expect(expected).to.include(actual)
    expect(expected).to.have(actual)

    with context.raises:
        expect(expected).to_not.contain(actual)

    with context.raises:
        expect(expected).to_not.include(actual)

    with context.raises:
        expect(expected).to_not.have(actual)


@expected_actual_params(stubs.CONTAIN_TYPE_ERROR)
def test_to_contain_type_error(expected, actual, context):
    with context.raises:
        expect(expected).to.contain(actual)


@expected_actual_params(stubs.CONTAIN_TYPE_ERROR)
def test_to_contained_in_type_error(expected, actual, context):
    with context.raises:
        expect(actual).to.be_contained_in(expected)
