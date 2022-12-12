from expycted import expect
from expycted.matchers import IsMatcher

from helpers.utils import expected_params
from helpers.stubs import NOT_TRUE, NOT_FALSE


def test_via_expect(context):
    true = expect(True)
    false = expect(False)

    assert isinstance(true.to.be_true, IsMatcher)
    assert isinstance(false.to.be_false, IsMatcher)

    true.to.be_true()
    true.to_not.be_false()

    false.to.be_false()
    false.to_not.be_true()

    with context.raises:
        true.to.be_false()

    with context.raises:
        false.to.be_true()


@expected_params(NOT_TRUE, extract_ids=False)
def test_not_true(expected, context):
    expect(expected).to_not.be_true()

    with context.raises:
        expect(expected).to.be_true()


@expected_params(NOT_FALSE, extract_ids=False)
def test_not_false(expected, context):
    expect(expected).to_not.be_false()

    with context.raises:
        expect(expected).to.be_false()
