import pickle
from typing import Any, Callable, Collection, Tuple

from expycted.internals.utils import to_not_fn

assertion_texts = {
    "equal": "Expected {value1} to equal {value2}",
    "be": "Expected {value1} to be {value2}",
    "contain": "Expected {value1} to contain {value2}",
    "be_contained_in": "Expected {value1} to be contained in {value2}",
    "be_empty": "Expected {value1} to be empty",
    "be_true": "Expected {value1} to be true",
    "be_false": "Expected {value1} to be false",
    "be_truthy": "Expected {value1} to be truthy",
    "be_falsey": "Expected {value1} to be falsey",
    "be_of_type": "Expected {value1} to be of type {value2}",
    "inherit": "Expected {value1} to inherit {value2}",
    "be_greater_than": "Expected {value1} to be greater than {value2}",
    "be_lesser_than": "Expected {value1} to be less than {value2}",
    "be_greater_or_equal_to": "Expected {value1} to be greater than or equal to {value2}",
    "be_lesser_or_equal_to": "Expected {value1} to be less than or equal to {value2}",
    "be_numeric": "Expected {value1} to be numeric",
}


class To:
    value: Any

    def __init__(self, value):
        self.value = value

    def _internal_has_len(self: Any) -> bool:
        try:
            len(self.value)
            return True
        except TypeError:
            return False

    def _internal_equal(self, something: Any) -> Tuple[bool, str]:
        return self.value == something, assertion_texts["equal"].format(
            value1=self.value, value2=something
        )

    def _internal_be(self, something: Any) -> Tuple[bool, str]:
        return any(
            [
                str(self.value) == str(something),
                pickle.dumps(self.value) == pickle.dumps(something),
                self.value == something,
            ]
        ), assertion_texts["be"].format(value1=self.value, value2=something)

    def _internal_contain(self, something: Any) -> Tuple[bool, str]:
        try:
            return something in self.value, assertion_texts["contain"].format(
                value1=self.value, value2=something
            )
        except Exception:
            raise AssertionError(
                f'Type "{type(self.value)} cannot contain {something}"'
            )

    def _internal_be_contained_in(self, something: Collection) -> Tuple[bool, str]:
        try:
            return self.value in something, assertion_texts["be_contained_in"].format(
                value1=self.value, value2=something
            )
        except Exception:
            raise AssertionError(
                f'Type "{type(something)} cannot contain {self.value}"'
            )

    def _internal_be_empty(self):
        try:
            iter(self.value)
            return not self.value, assertion_texts["be_empty"].format(value1=self.value)
        except TypeError:
            raise AssertionError(
                f"Emptiness of '{type(self.value)}' object doesn't make sense"
            )

    def _internal_be_true(self) -> Tuple[bool, str]:
        return self.value is True, assertion_texts["be_true"].format(value1=self.value)

    def _internal_be_false(self) -> Tuple[bool, str]:
        return self.value is False, assertion_texts["be_false"].format(
            value1=self.value
        )

    def _internal_be_truthy(self) -> Tuple[bool, str]:
        return True if self.value else False, assertion_texts["be_truthy"].format(
            value1=self.value
        )

    def _internal_be_falsey(self) -> Tuple[bool, str]:
        return True if not self.value else False, assertion_texts["be_falsey"].format(
            value1=self.value
        )

    def _internal_be_of_type(self, something: type) -> Tuple[bool, str]:
        return type(self.value) is something, assertion_texts["be_of_type"].format(
            value1=self.value, value2=something
        )

    def _internal_inherit(self, something: type) -> Tuple[bool, str]:
        try:
            return issubclass(type(self.value), something), assertion_texts[
                "inherit"
            ].format(value1=self.value, value2=something)
        except Exception:
            raise AssertionError("Second argument must be a class, not an instance")

    def _internal_be_greater_than(self, something: Any) -> Tuple[bool, str]:
        return self.value > something, assertion_texts["be_greater_than"].format(
            value1=self.value, value2=something
        )

    def _internal_be_lesser_than(self, something: Any) -> Tuple[bool, str]:
        return self.value < something, assertion_texts["be_lesser_than"].format(
            value1=self.value, value2=something
        )

    def _internal_be_greater_or_equal_to(self, something: Any) -> Tuple[bool, str]:
        return self.value >= something, assertion_texts[
            "be_greater_or_equal_to"
        ].format(value1=self.value, value2=something)

    def _internal_be_lesser_or_equal_to(self, something: Any) -> Tuple[bool, str]:
        return self.value <= something, assertion_texts["be_lesser_or_equal_to"].format(
            value1=self.value, value2=something
        )

    def _internal_be_numeric(self: Any) -> Tuple[bool, str]:
        assertion_text = assertion_texts["be_numeric"].format(value1=self.value)
        if type(self.value) in [int, float, complex]:
            return True, assertion_text
        elif type(self.value) is str:

            try:
                float(self.value)
                print(float(self.value))
                return True, assertion_text
            except Exception:
                return False, assertion_text
        return False, assertion_text

    def equal(self, something: Any) -> None:
        """Checks whether that the value is equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        res = self._internal_equal(something)
        assert res[0], res[1]

    def be(self, something: Any) -> None:
        """Checks whether the value is 'softly' equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """

        res = self._internal_be(something)
        assert res[0], res[1]

    def contain(self, something: Any) -> None:
        """Checks whether the value contains something

        Args:
            something (Any): The value to be contained

        Returns:
            bool: Result
        """
        res = self._internal_contain(something)
        assert res[0], res[1]

    def be_contained_in(self, something: Collection) -> None:
        """Checks whether the value is contained in something

        Args:
            something (Any): The value to contain something

        Returns:
            bool: Result
        """
        res = self._internal_be_contained_in(something)
        assert res[0], res[1]

    def be_empty(self) -> None:
        """Checks whether the value is empty

        Returns:
            bool: Result
        """
        res = self._internal_be_empty()
        assert res[0], res[1]

    def be_true(self) -> None:
        """Checks whether the value is true

        Returns:
            bool: Result
        """
        res = self._internal_be_true()
        assert res[0], res[1]

    def be_false(self) -> None:
        """Checks whether the value is false

        Returns:
            bool: Result
        """
        res = self._internal_be_false()
        assert res[0], res[1]

    def be_truthy(self) -> None:
        """Checks whether the value is truthy

        Returns:
            bool: Result
        """
        res = self._internal_be_truthy()
        assert res[0], res[1]

    def be_falsey(self) -> None:
        """Checks whether the value is falsey

        Returns:
            bool: Result
        """
        res = self._internal_be_falsey()
        assert res[0], res[1]

    def be_of_type(self, something: type) -> None:
        """Checks whether the value is of provided type

        Args:
            something (type): Type to be checked against

        Returns:
            bool: Result
        """
        res = self._internal_be_of_type(something)
        assert res[0], res[1]

    def inherit(self, something: type) -> None:
        """Checks whether the value inherits from provided type

        Args:
            something (type): Type to inherit from

        Returns:
            bool: Result
        """
        res = self._internal_inherit(something)
        assert res[0], res[1]

    def be_greater_than(self, something: Any) -> None:
        """Check whether the value is greater than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        res = self._internal_be_greater_than(something)
        assert res[0], res[1]

    def be_lesser_than(self, something: Any) -> None:
        """Check whether the value is lesser than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        res = self._internal_be_lesser_than(something)
        assert res[0], res[1]

    def be_greater_or_equal_to(self, something: Any) -> None:
        """Check whether the value is greater than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        res = self._internal_be_greater_or_equal_to(something)
        assert res[0], res[1]

    def be_lesser_or_equal_to(self, something: Any) -> None:
        """Check whether the value is lesser than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        res = self._internal_be_lesser_or_equal_to(something)
        assert res[0], res[1]

    def be_numeric(self) -> None:
        """Check whether the value is numeric

        Returns:
            bool: Result
        """
        res = self._internal_be_numeric()
        assert res[0], res[1]

    # Aliases

    be_a_number = be_numeric

    be_lesser = be_less = be_less_than = be_lesser_than
    be_lesser_or_equal = (
        be_less_or_equal
    ) = be_less_than_or_equal_to = be_lesser_than_or_equal_to = be_lesser_or_equal_to

    be_greater_or_equal = be_greater_than_or_equal_to = be_greater_or_equal_to
    be_greater = be_greater_than

    be_falsy = be_falsish = be_falsey
    be_truey = be_trueish = be_truthy

    be_in = be_included_in = be_contained_in
    have = include = contain

    be_equal_to = equal
    be_type = have_type = be_of_type
    be_subclass_of = have_parent = inherit


class ToNot(To):
    value: Any

    def __init__(self, value: Any):
        super().__init__(value)
        to = To(value)
        for i in list(filter(lambda x: x.startswith("_internal_"), dir(to))):
            expect_method = getattr(to, i)
            self.__setattr__(i.replace("_internal_", ""), to_not_fn(expect_method))
