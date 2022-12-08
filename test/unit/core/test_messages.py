import pytest
from enum import Enum
from expycted.core.messages import Message
from helpers.stubs import PERSON, Day

def test_full_lead_line():
    message = Message("equal", operation='==')

    assert message.lead(actual=4, expected=5) == "expect(4).to.equal(5) # Using `==`"


def test_full_lead_line_negated():
    message = Message("equal", operation='==', negated=True)

    assert message.lead(actual=4, expected=5) == "expect(4).to_not.equal(5) # Using `==`"


def test_lead_line_without_operation():
    message = Message("equal")

    assert message.lead(actual=4, expected=5) == "expect(4).to.equal(5)"


def test_lead_line_with_none_as_expected():
    message = Message("equal")

    assert message.lead(actual=4, expected=None) == "expect(4).to.equal(None)"


def test_lead_line_without_expected():
    message = Message("be_empty")

    assert message.lead(actual=[4,1]) == "expect([4, 1]).to.be_empty()"
