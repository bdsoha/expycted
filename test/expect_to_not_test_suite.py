from expycted import expect

from helpers import stubs
from helpers.utils import expected_actual_params, expected_params


@expected_actual_params(stubs.NOT_EQUAL)
def test_to_not_equal_success(expected, actual, context):
    expect(expected).to_not.equal(actual)

    with context.raises:
        expect(expected).to.equal(actual)


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


@expected_params(stubs.NOT_EMPTY, extract_ids=False)
def test_to_not_be_empty(expected, context):
    expect(expected).to_not.be_empty()

    with context.raises:
        expect(expected).to.be_empty()


@expected_params(stubs.NOT_TRUE, extract_ids=False)
def test_to_not_be_true(expected, context):
    expect(expected).to_not.be_true()

    with context.raises:
        expect(expected).to.be_true()


@expected_params(stubs.NOT_FALSE, extract_ids=False)
def test_to_not_be_false(expected, context):
    expect(expected).to_not.be_false()

    with context.raises:
        expect(expected).to.be_false()


@expected_params(stubs.NOT_TRUETHY, extract_ids=False)
def test_to_not_be_truthy(expected, context):
    expect(expected).to_not.be_truthy()

    with context.raises:
        expect(expected).to.be_truthy()


@expected_params(stubs.NOT_FALSEY, extract_ids=False)
def test_to_not_be_falsey(expected, context):
    expect(expected).to_not.be_falsey()

    with context.raises:
        expect(expected).to.be_falsey()


@expected_actual_params(stubs.NOT_TYPE, extract_ids=False)
def test_to_not_be_of_type(expected, actual, context):
    expect(expected).to_not.be_of_type(actual)

    with context.raises:
        expect(expected).to.be_of_type(actual)


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


@expected_params(stubs.NOT_LIST, extract_ids=False)
def test_to_not_be_list(expected, context):
    expect(expected).to_not.be_list()

    with context.raises:
        expect(expected).to.be_list()


@expected_params(stubs.NOT_BOOL, extract_ids=False)
def test_to_not_be_bool(expected, context):
    expect(expected).to_not.be_bool()

    with context.raises:
        expect(expected).to.be_bool()


@expected_params(stubs.NOT_INT, extract_ids=False)
def test_to_not_be_int(expected, context):
    expect(expected).to_not.be_int()

    with context.raises:
        expect(expected).to.be_int()


@expected_params(stubs.NOT_FLOAT, extract_ids=False)
def test_to_not_be_float(expected, context):
    expect(expected).to_not.be_float()

    with context.raises:
        expect(expected).to.be_float()


@expected_params(stubs.NOT_STR, extract_ids=False)
def test_to_not_be_str(expected, context):
    expect(expected).to_not.be_str()

    with context.raises:
        expect(expected).to.be_str()
