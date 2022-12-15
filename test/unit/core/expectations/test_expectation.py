from __future__ import annotations

from expycted.core.expectations import Expectation


def test_is_negated():
    expectation = Expectation(1)

    assert expectation.is_negated is False

    assert expectation.to_not
    assert expectation.is_negated is True

    assert expectation.to
    assert expectation.is_negated is False
