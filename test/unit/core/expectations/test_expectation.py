from __future__ import annotations

from expycted import expect
from expycted.core.expectations import Expectation


def test_is_negated():
    expectation = Expectation(1)

    assert expectation.is_negated is False

    assert expectation.to_not
    assert expectation.is_negated is True

    assert expectation.to
    assert expectation.is_negated is False


def test_chaining():
    expect_object = expect.value(1)

    assert expect_object.to is expect_object
    assert expect_object.and_to is expect_object
    assert expect_object.to_not is expect_object
    assert expect_object.and_not is expect_object
    assert expect_object.and_to_not is expect_object

    expect([1, 2, 3]).to_not.contain(7).and_to.contain(3)
