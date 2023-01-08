from __future__ import annotations

from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params, expected_params


@expected_actual_params(stubs.BE)
def test_to_be(expected, actual, context):
    expect(expected).to.be(actual)

    with context.raises:
        expect(expected).to_not.be(actual)


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


@expected_actual_params(stubs.CONTAIN)
def test_to_be_contained_in(expected, actual, context):
    expect(actual).to.be_contained_in(expected)
    expect(actual).to.be_included_in(expected)
    expect(actual).to.be_in(expected)

    with context.raises:
        expect(actual).to_not.be_contained_in(expected)

    with context.raises:
        expect(actual).to_not.be_included_in(expected)

    with context.raises:
        expect(actual).to_not.be_in(expected)


@expected_actual_params(stubs.CONTAIN_TYPE_ERROR)
def test_to_contained_in_type_error(expected, actual, context):
    with context.raises:
        expect(actual).to.be_contained_in(expected)


@expected_actual_params(stubs.INHERIT, extract_ids=False)
def test_to_inherit(expected, actual, context):
    expect(expected).to.inherit(actual)
    expect(expected).to.have_parent(actual)
    expect(expected).to.be_subclass_of(actual)

    with context.raises:
        expect(expected).to_not.inherit(actual)

    with context.raises:
        expect(expected).to_not.have_parent(actual)

    with context.raises:
        expect(expected).to_not.be_subclass_of(actual)


@expected_actual_params(stubs.INHERIT_TYPE_ERROR, extract_ids=False)
def test_to_inherit_type_error(expected, actual, context):
    with context.raises:
        expect(expected).to.inherit(actual)
