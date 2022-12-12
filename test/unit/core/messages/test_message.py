from expycted.core.messages import DetailMessage, Message


def test_signature_full():
    message = Message("equal", operation="==")

    assert (
        message.signature(actual=4, expected=5) == "expect(4).to.equal(5) # Using `==`"
    )


def test_signature_full_and_negated():
    message = Message("equal", operation="==", negated=True)

    assert (
        message.signature(actual=4, expected=5)
        == "expect(4).to_not.equal(5) # Using `==`"
    )


def test_signature_without_operation():
    message = Message("equal")

    assert message.signature(actual=4, expected=5) == "expect(4).to.equal(5)"


def test_signature_with_none_as_expected():
    message = Message("equal")

    assert message.signature(actual=4, expected=None) == "expect(4).to.equal(None)"


def test_signature_without_exected():
    message = Message("be_empty")

    assert message.signature(actual=[4, 1]) == "expect([4, 1]).to.be_empty()"


def test_details_default():
    message = Message("equal")

    assert message.details(actual="4", expected=4) == 'Expected\t: 4\nActual\t: "4"'


def test_details_negated():
    message = Message("equal", operation="==", negated=True)

    assert message.details(actual="4", expected=4) == 'Expected\t: 4\nActual\t: "4"'


def test_details_with_detail_message():
    message = Message(
        "be_empty",
        negated=True,
        message=DetailMessage(expected="Expected {to} be empty"),
    )

    details = message.details(actual=[4, 1])

    assert details == "Expected to not be empty\nActual\t: [4, 1]"


def test_details_with_detail_message_as_string():
    message = Message(
        "be_empty",
        negated=True,
        message="Expected {to} {method_split}, but was actually {actual}",
    )

    details = message.details(actual=[4, 1])

    assert details == "Expected to not be empty, but was actually [4, 1]"
