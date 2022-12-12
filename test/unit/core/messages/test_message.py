from expycted.core.messages import DetailMessage, Message


class TestSignature:
    def test_full(self):
        message = Message("equal", operation="==")

        assert (
            message.signature(actual=4, expected=5)
            == "expect(4).to.equal(5) # Using `==`"
        )

    def test_full_and_negated(self):
        message = Message("equal", operation="==", negated=True)

        assert (
            message.signature(actual=4, expected=5)
            == "expect(4).to_not.equal(5) # Using `==`"
        )

    def test_without_operation(self):
        message = Message("equal")

        assert message.signature(actual=4, expected=5) == "expect(4).to.equal(5)"

    def test_with_none_as_expected(self):
        message = Message("equal")

        assert message.signature(actual=4, expected=None) == "expect(4).to.equal(None)"

    def test_without_expected(self):
        message = Message("be_empty")

        assert message.signature(actual=[4, 1]) == "expect([4, 1]).to.be_empty()"


class TestDetails:
    def test_default(self):
        message = Message("equal")

        assert message.details(actual="4", expected=4) == 'Expected\t: 4\nActual\t: "4"'

    def test_negated(self):
        message = Message("equal", operation="==", negated=True)

        assert message.details(actual="4", expected=4) == 'Expected\t: 4\nActual\t: "4"'

    def test_with_detail_message(self):
        message = Message(
            "be_empty",
            negated=True,
            message=DetailMessage(expected="Expected {to} be empty"),
        )

        details = message.details(actual=[4, 1])

        assert details == "Expected to not be empty\nActual\t: [4, 1]"

    def test_with_detail_message_as_string(self):
        message = Message(
            "be_empty",
            negated=True,
            message="Expected {to} {method_split}, but was actually {actual}",
        )

        details = message.details(actual=[4, 1])

        assert details == "Expected to not be empty, but was actually [4, 1]"
