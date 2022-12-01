from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params, expected_params


@expected_actual_params(stubs.EQUAL)
def test_to_equal(expected, actual, context):
    expect(expected).to.equal(actual)
    expect(expected).to.be_equal_to(actual)

    with context.raises:
        expect(expected).to_not.equal(actual)

    with context.raises:
        expect(expected).to_not.be_equal_to(actual)


@expected_actual_params(stubs.BE)
def test_to_be(expected, actual, context):
    expect(expected).to.be(actual)

    with context.raises:
        expect(expected).to_not.be(actual)


@expected_actual_params(stubs.CONTAIN)
def test_to_contain(expected, actual, context):
    expect(expected).to.contain(actual)

    with context.raises:
        expect(expected).to_not.contain(actual)


@expected_actual_params(stubs.CONTAIN_TYPE_ERROR)
def test_to_contain_type_error(expected, actual, context):
    with context.raises:
        expect(expected).to.contain(actual)


@expected_actual_params(stubs.CONTAIN)
def test_to_be_contained_in(expected, actual, context):
    expect(actual).to.be_contained_in(expected)

    with context.raises:
        expect(actual).to_not.be_contained_in(expected)


@expected_actual_params(stubs.CONTAIN_TYPE_ERROR)
def test_to_contained_in_type_error(expected, actual, context):
    with context.raises:
        expect(actual).to.be_contained_in(expected)


@expected_params(stubs.EMPTY, extract_ids=False)
def test_to_be_empty(expected, context):
    expect(expected).to.be_empty()

    with context.raises:
        expect(expected).to_not.be_empty()


@expected_params(stubs.NOT_EMPTY_TYPE_ERROR, extract_ids=False)
def test_to_be_empty_type_error(expected, context):
    with context.raises:
        expect(expected).to.be_empty()


@expected_params(stubs.TRUE, extract_ids=False)
def test_to_be_true(expected, context):
    expect(expected).to.be_true()

    with context.raises:
        expect(expected).to_not.be_true()


@expected_params(stubs.FALSE, extract_ids=False)
def test_to_be_false(expected, context):
    expect(expected).to.be_false()

    with context.raises:
        expect(expected).to_not.be_false()


@expected_params(stubs.TRUETHY, extract_ids=False)
def test_to_be_truthy(expected, context):
    expect(expected).to.be_truthy()

    with context.raises:
        expect(expected).to_not.be_truthy()


@expected_params(stubs.FALSEY, extract_ids=False)
def test_to_be_falsey(expected, context):
    expect(expected).to.be_falsey()

    with context.raises:
        expect(expected).to_not.be_falsey()


@expected_actual_params(stubs.TYPE, extract_ids=False)
def test_to_be_of_type(expected, actual, context):
    expect(expected).to.be_of_type(actual)

    with context.raises:
        expect(expected).to_not.be_of_type(actual)


@expected_actual_params(stubs.INHERIT, extract_ids=False)
def test_to_inherit(expected, actual, context):
    expect(expected).to.inherit(actual)

    with context.raises:
        expect(expected).to_not.inherit(actual)


@expected_actual_params(stubs.INHERIT_TYPE_ERROR, extract_ids=False)
def test_to_inherit_type_error(expected, actual, context):
    with context.raises:
        expect(expected).to.inherit(actual)


@expected_actual_params(stubs.GREATER_THAN, extract_ids=False)
def test_to_be_greater_than(expected, actual, context):
    expect(expected).to.be_greater_than(actual)

    with context.raises:
        expect(expected).to_not.be_greater_than(actual)


@expected_actual_params(stubs.LESS_THAN, extract_ids=False)
def test_to_be_lesser_than(expected, actual, context):
    expect(expected).to.be_lesser_than(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_than(actual)


@expected_actual_params(stubs.GREATER_THAN_OR_EQUAL, extract_ids=False)
def test_to_be_greater_than_or_equal_to(expected, actual, context):
    expect(expected).to.be_greater_than_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_greater_than_or_equal_to(actual)


@expected_actual_params(stubs.LESS_THAN_OR_EQUAL, extract_ids=False)
def test_to_be_lesser_or_equal_to(expected, actual, context):
    expect(expected).to.be_lesser_or_equal_to(actual)

    with context.raises:
        expect(expected).to_not.be_lesser_or_equal_to(actual)


@expected_params(stubs.NUMERIC, extract_ids=False)
def test_to_be_numeric(expected, context):
    expect(expected).to.be_numeric()

    with context.raises:
        expect(expected).to_not.be_numeric()
