from __future__ import annotations

from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params, expected_params


@expected_actual_params(stubs.NOT_BE)
def test_to_not_be(expected, actual, context):
    expect(expected).to_not.be(actual)

    with context.raises:
        expect(expected).to.be(actual)


@expected_actual_params(stubs.NOT_CONTAIN)
def test_to_not_contain(expected, actual, context):
    expect(expected).to_not.contain(actual)

    with context.raises:
        expect(expected).to.contain(actual)


@expected_actual_params(stubs.NOT_CONTAIN)
def test_to_not_be_contained_in(expected, actual, context):
    expect(actual).to_not.be_contained_in(expected)

    with context.raises:
        expect(actual).to.be_contained_in(expected)


@expected_actual_params(stubs.NOT_INHERIT, extract_ids=False)
def test_to_not_inherit(expected, actual, context):
    expect(expected).to_not.inherit(actual)

    with context.raises:
        expect(expected).to.inherit(actual)


@expected_actual_params(stubs.LESS_THAN, extract_ids=False)
def test_to_not_be_greater_than(expected, actual, context):
    expect(expected).to_not.be_greater_than(actual)

    with context.raises:
        expect(expected).to.be_greater_than(actual)


@expected_actual_params(stubs.GREATER_THAN, extract_ids=False)
def test_to_not_be_lesser_than(expected, actual, context):
    expect(expected).to_not.be_lesser_than(actual)

    with context.raises:
        expect(expected).to.be_lesser_than(actual)


@expected_params(stubs.NOT_NUMERIC, extract_ids=False)
def test_to_not_be_numeric(expected, context):
    expect(expected).to_not.be_numeric()

    with context.raises:
        expect(expected).to.be_numeric()
