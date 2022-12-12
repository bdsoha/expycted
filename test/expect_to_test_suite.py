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


@expected_params(stubs.TRUETHY, extract_ids=False)
def test_to_be_truthy(expected, context):
    expect(expected).to.be_truthy()
    expect(expected).to.be_trueish()
    expect(expected).to.be_truey()

    with context.raises:
        expect(expected).to_not.be_truthy()

    with context.raises:
        expect(expected).to_not.be_trueish()

    with context.raises:
        expect(expected).to_not.be_truey()


@expected_params(stubs.FALSEY, extract_ids=False)
def test_to_be_falsey(expected, context):
    expect(expected).to.be_falsey()
    expect(expected).to.be_falsish()
    expect(expected).to.be_falsy()

    with context.raises:
        expect(expected).to_not.be_falsey()

    with context.raises:
        expect(expected).to_not.be_falsish()

    with context.raises:
        expect(expected).to_not.be_falsy()


@expected_actual_params(stubs.TYPE, extract_ids=False)
def test_to_be_of_type(expected, actual, context):
    expect(expected).to.be_of_type(actual)
    expect(expected).to.have_type(actual)
    expect(expected).to.be_type(actual)

    with context.raises:
        expect(expected).to_not.be_of_type(actual)

    with context.raises:
        expect(expected).to_not.have_type(actual)

    with context.raises:
        expect(expected).to_not.be_type(actual)


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


@expected_actual_params(stubs.GREATER_THAN, extract_ids=False)
def test_to_be_greater_than(expected, actual, context):
    expect(expected).to.be_greater_than(actual)
    expect(expected).to.be_greater(actual)

    with context.raises:
        expect(expected).to_not.be_greater_than(actual)

    with context.raises:
        expect(expected).to_not.be_greater(actual)


@expected_actual_params(stubs.LESS_THAN, extract_ids=False)
def test_to_be_lesser_than(expected, actual, context):
    expect(expected).to.be_lesser_than(actual)
    expect(expected).to.be_less_than(actual)
    expect(expected).to.be_less(actual)
    expect(expected).to.be_lesser(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_than(actual)

    with context.raises:
        expect(expected).to_not.be_less_than(actual)

    with context.raises:
        expect(expected).to_not.be_less(actual)

    with context.raises:
        expect(expected).to_not.be_lesser(actual)


@expected_actual_params(stubs.GREATER_THAN_OR_EQUAL, extract_ids=False)
def test_to_be_greater_than_or_equal_to(expected, actual, context):
    expect(expected).to.be_greater_than_or_equal_to(actual)
    expect(expected).to.be_greater_than_or_equal_to(actual)
    expect(expected).to.be_greater_or_equal(actual)

    with context.raises:
        expect(expected).to_not.be_greater_than_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_greater_than_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_greater_or_equal(actual)


@expected_actual_params(stubs.LESS_THAN_OR_EQUAL, extract_ids=False)
def test_to_be_lesser_or_equal_to(expected, actual, context):
    expect(expected).to.be_lesser_or_equal_to(actual)
    expect(expected).to.be_lesser_than_or_equal_to(actual)
    expect(expected).to.be_less_than_or_equal_to(actual)
    expect(expected).to.be_less_or_equal(actual)
    expect(expected).to.be_lesser_or_equal(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_than_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_less_than_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_less_or_equal(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_or_equal(actual)


@expected_params(stubs.NUMERIC, extract_ids=False)
def test_to_be_numeric(expected, context):
    expect(expected).to.be_numeric()
    expect(expected).to.be_a_number()

    with context.raises:
        expect(expected).to_not.be_numeric()

    with context.raises:
        expect(expected).to_not.be_a_number()
