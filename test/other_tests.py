from __future__ import annotations

from expycted import expect


def test_method_chaining():
    expect_object = expect.value(1)

    assert expect_object.to is expect_object
    assert expect_object.and_to is expect_object
    assert expect_object.to_not is expect_object
    assert expect_object.and_not is expect_object
    assert expect_object.and_to_not is expect_object

    expect([1, 2, 3]).to_not.contain(7).and_to.contain(3)
