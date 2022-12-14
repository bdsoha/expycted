from __future__ import annotations

import pytest

from expycted import expect


@pytest.mark.parametrize(
    "v1,true",
    [
        (1, False),
        (3, False),
        (3.2, False),
        ("a", True),
        ([1, 2], True),
        (set(), True),
        (tuple(), True),
        ("123", True),
        (lambda x: x, False),
    ],
)
def test_has_len(v1, true):
    assert expect(v1).to._internal_has_len() == true


def test_to_expect_value():
    expect_object = expect.value(1)
    assert isinstance(expect_object, expect)
    assert expect_object.expected == 1
    assert expect_object.expected == 1


def test_method_chaining():
    expect_object = expect.value(1)

    assert expect_object.to is expect_object
    assert expect_object.and_to is expect_object
    assert expect_object.to_not is expect_object
    assert expect_object.and_not is expect_object
    assert expect_object.and_to_not is expect_object

    expect([1, 2, 3]).to_not.contain(7).and_to.contain(3)


def test_negation_chaining():
    expect_object = expect.value(1)

    assert expect_object.to.negate is False
    assert expect_object.to_not.negate is True
    assert expect_object.to_not.to.negate is False
