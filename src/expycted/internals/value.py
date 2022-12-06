import pickle
from typing import Any, Collection, Tuple

from expycted.internals.utils import assertion, hidetraceback
from expycted.internals.base import BaseExpectation


class Value(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "equal": "Expected {expected} to equal {actual}",
        "be": "Expected {expected} to be {actual}",
        "contain": "Expected {expected} to contain {actual}",
        "be_contained_in": "Expected {expected} to be contained in {actual}",
        "be_empty": "Expected {expected} to be empty",
        "be_true": "Expected {expected} to be true",
        "be_false": "Expected {expected} to be false",
        "be_truthy": "Expected {expected} to be truthy",
        "be_falsey": "Expected {expected} to be falsey",
        "be_of_type": "Expected {expected} to be of type {actual}",
        "inherit": "Expected {expected} to inherit {actual}",
        "be_greater_than": "Expected {expected} to be greater than {actual}",
        "be_lesser_than": "Expected {expected} to be less than {actual}",
        "be_greater_or_equal_to": "Expected {expected} to be greater than or equal to {actual}",
        "be_lesser_or_equal_to": "Expected {expected} to be less than or equal to {actual}",
        "be_numeric": "Expected {expected} to be numeric",
        "be_callable": "Expected {expected} to be callable",
    }

    def _internal_has_len(self: Any) -> bool:
        try:
            len(self.expected)
            return True
        except TypeError:
            return False

    def _internal_equal(self, actual: Any) -> Tuple[bool, str]:
        return self.expected == actual, self._message("equal", actual)

    def _internal_be(self, actual: Any) -> Tuple[bool, str]:
        return any(
            [
                str(self.expected) == str(actual),
                pickle.dumps(self.expected) == pickle.dumps(actual),
                self.expected == actual,
            ]
        ), self._message("be", actual)

    def _internal_contain(self, actual: Any) -> Tuple[bool, str]:
        try:
            return actual in self.expected, self._message("contain", actual)
        except Exception:
            raise AssertionError(
                f'Type "{type(self.expected)} cannot contain {actual}"'
            )

    def _internal_be_contained_in(self, actual: Collection) -> Tuple[bool, str]:
        try:
            return self.expected in actual, self._message("be_contained_in", actual)
        except Exception:
            raise AssertionError(
                f'Type "{type(actual)} cannot contain {self.expected}"'
            )

    def _internal_be_empty(self):
        try:
            iter(self.expected)
            return not self.expected, self._message("be_empty")
        except TypeError:
            raise AssertionError(
                f"Emptiness of '{type(self.expected)}' object doesn't make sense"
            )

    def _internal_be_true(self) -> Tuple[bool, str]:
        return self.expected is True, self._message("be_true")

    def _internal_be_false(self) -> Tuple[bool, str]:
        return self.expected is False, self._message("be_false")

    def _internal_be_truthy(self) -> Tuple[bool, str]:
        return bool(self.expected), self._message("be_truthy")

    def _internal_be_falsey(self) -> Tuple[bool, str]:
        return not bool(self.expected), self._message("be_falsey")

    def _internal_be_of_type(self, actual: type) -> Tuple[bool, str]:
        return type(self.expected) is actual, self._message("be_of_type", actual)

    def _internal_inherit(self, actual: type) -> Tuple[bool, str]:
        try:
            return issubclass(type(self.expected), actual), self._message("inherit", actual)
        except Exception:
            raise AssertionError("Second argument must be a class, not an instance")

    def _internal_be_greater_than(self, actual: Any) -> Tuple[bool, str]:
        return self.expected > actual, self._message("be_greater_than", actual)

    def _internal_be_lesser_than(self, actual: Any) -> Tuple[bool, str]:
        return self.expected < actual, self._message("be_lesser_than", actual)

    def _internal_be_greater_or_equal_to(self, actual: Any) -> Tuple[bool, str]:
        return self.expected >= actual, self._message("be_greater_or_equal_to", actual)

    def _internal_be_lesser_or_equal_to(self, actual: Any) -> Tuple[bool, str]:
        return self.expected <= actual, self._message("be_lesser_or_equal_to", actual)

    def _internal_be_numeric(self: Any) -> Tuple[bool, str]:
        assertion_text = self._message("be_numeric")

        if type(self.expected) in [int, float, complex]:
            return True, assertion_text

        if type(self.expected) is str:
            try:
                float(self.expected)
                return True, assertion_text
            except Exception:
                pass

        return False, assertion_text

    def _internal_be_callable(self) -> Tuple[bool, str]:
        return callable(self.expected), self._message("be_callable")

    @assertion
    def equal(self, actual: Any) -> None:
        """Checks whether that the value is equal to something

        Args:
            actual (Any): The value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def be(self, actual: Any) -> None:
        """Checks whether the value is 'softly' equal to something

        Args:
            actual (Any): The value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def contain(self, actual: Any) -> None:
        """Checks whether the value contains something

        Args:
            actual (Any): The value to be contained

        Returns:
            bool: Result
        """

    @assertion
    def be_contained_in(self, actual: Collection) -> None:
        """Checks whether the value is contained in something

        Args:
            actual (Any): The value to contain something

        Returns:
            bool: Result
        """

    @assertion
    def be_empty(self) -> None:
        """Checks whether the value is empty

        Returns:
            bool: Result
        """

    @assertion
    def be_true(self) -> None:
        """Checks whether the value is true

        Returns:
            bool: Result
        """

    @assertion
    def be_false(self) -> None:
        """Checks whether the value is false

        Returns:
            bool: Result
        """

    @assertion
    def be_truthy(self) -> None:
        """Checks whether the value is truthy

        Returns:
            bool: Result
        """

    @assertion
    def be_falsey(self) -> None:
        """Checks whether the value is falsey

        Returns:
            bool: Result
        """

    @assertion
    def be_of_type(self, actual: type) -> None:
        """Checks whether the value is of provided type

        Args:
            actual (type): Type to be checked against

        Returns:
            bool: Result
        """

    @assertion
    def inherit(self, actual: type) -> None:
        """Checks whether the value inherits from provided type

        Args:
            actual (type): Type to inherit from

        Returns:
            bool: Result
        """

    @assertion
    def be_greater_than(self, actual: Any) -> None:
        """Check whether the value is greater than something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def be_lesser_than(self, actual: Any) -> None:
        """Check whether the value is lesser than something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def be_greater_or_equal_to(self, actual: Any) -> None:
        """Check whether the value is greater than or equal to something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def be_lesser_or_equal_to(self, actual: Any) -> None:
        """Check whether the value is lesser than or equal to something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion
    def be_numeric(self) -> None:
        """Check whether the value is numeric

        Returns:
            bool: Result
        """

    @assertion
    def be_callable(self) -> None:
        """Check whether the value is callable

        Returns:
            bool: Result
        """


    @hidetraceback
    def be_list(self) -> None:
        """Check whether the value is a list

        Returns:
            bool: Result
        """
        return self.be_of_type(list)


    @hidetraceback
    def be_tuple(self) -> None:
        """Check whether the value is a tuple

        Returns:
            bool: Result
        """
        return self.be_of_type(tuple)


    @hidetraceback
    def be_set(self) -> None:
        """Check whether the value is a set

        Returns:
            bool: Result
        """
        return self.be_of_type(set)


    @hidetraceback
    def be_dict(self) -> None:
        """Check whether the value is a dict

        Returns:
            bool: Result
        """
        return self.be_of_type(dict)


    @hidetraceback
    def be_bool(self) -> None:
        """Check whether the value is a bool

        Returns:
            bool: Result
        """
        return self.be_of_type(bool)

    @hidetraceback
    def be_int(self) -> None:
        """Check whether the value is an int

        Returns:
            bool: Result
        """
        return self.be_of_type(int)

    @hidetraceback
    def be_float(self) -> None:
        """Check whether the value is a float

        Returns:
            bool: Result
        """
        return self.be_of_type(float)

    @hidetraceback
    def be_str(self) -> None:
        """Check whether the value is a str

        Returns:
            bool: Result
        """
        return self.be_of_type(str)


    @hidetraceback
    def be_none(self) -> None:
        """Check whether the value is None

        Returns:
            bool: Result
        """
        return self.be_of_type(type(None))

    # Aliases

    be_a_number = be_numeric

    be_a_list = be_list
    be_a_bool = be_bool
    be_an_int = be_int
    be_a_float = be_float
    be_a_str = be_str

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
