import pickle
from typing import Any, Collection, Tuple

from expycted.internals.utils import assertion, hidetraceback
from expycted.internals.base import BaseExpectation


class Value(BaseExpectation):
    _ASSERTION_MESSAGES = {
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
        "be_numeric_strict": "Expected {value1} to be strictly a number type",
        "be_callable": "Expected {value1} to be callable",
    }

    def _internal_has_len(self: Any) -> bool:
        try:
            len(self.value)
            return True
        except TypeError:
            return False

    def _internal_equal(self, something: Any) -> Tuple[bool, str]:
        return self.value == something, self._message("equal", something)

    def _internal_be(self, something: Any) -> Tuple[bool, str]:
        return any(
            [
                str(self.value) == str(something),
                pickle.dumps(self.value) == pickle.dumps(something),
                self.value == something,
            ]
        ), self._message("be", something)

    def _internal_contain(self, something: Any) -> Tuple[bool, str]:
        try:
            return something in self.value, self._message("contain", something)
        except Exception:
            raise AssertionError(
                f'Type "{type(self.value)} cannot contain {something}"'
            )

    def _internal_be_contained_in(self, something: Collection) -> Tuple[bool, str]:
        try:
            return self.value in something, self._message("be_contained_in", something)
        except Exception:
            raise AssertionError(
                f'Type "{type(something)} cannot contain {self.value}"'
            )

    def _internal_be_empty(self):
        try:
            iter(self.value)
            return not self.value, self._message("be_empty")
        except TypeError:
            raise AssertionError(
                f"Emptiness of '{type(self.value)}' object doesn't make sense"
            )

    def _internal_be_true(self) -> Tuple[bool, str]:
        return self.value is True, self._message("be_true")

    def _internal_be_false(self) -> Tuple[bool, str]:
        return self.value is False, self._message("be_false")

    def _internal_be_truthy(self) -> Tuple[bool, str]:
        return True if self.value else False, self._message("be_truthy")

    def _internal_be_falsey(self) -> Tuple[bool, str]:
        return True if not self.value else False, self._message("be_falsey")

    def _internal_be_of_type(self, something: type) -> Tuple[bool, str]:
        return type(self.value) is something, self._message("be_of_type", something)

    def _internal_inherit(self, something: type) -> Tuple[bool, str]:
        try:
            return issubclass(type(self.value), something), self._message("inherit", something)
        except Exception:
            raise AssertionError("Second argument must be a class, not an instance")

    def _internal_be_greater_than(self, something: Any) -> Tuple[bool, str]:
        return self.value > something, self._message("be_greater_than", something)

    def _internal_be_lesser_than(self, something: Any) -> Tuple[bool, str]:
        return self.value < something, self._message("be_lesser_than", something)

    def _internal_be_greater_or_equal_to(self, something: Any) -> Tuple[bool, str]:
        return self.value >= something, self._message("be_greater_or_equal_to", something)

    def _internal_be_lesser_or_equal_to(self, something: Any) -> Tuple[bool, str]:
        return self.value <= something, self._message("be_lesser_or_equal_to", something)

    def _internal_be_numeric(self: Any, strict=False) -> Tuple[bool, str]:
        assertion_text = self._message("be_numeric")
        if type(self.value) in [int, float, complex]:
            return True, assertion_text
        
        if type(self.value) is str and strict:
            return False, self._message("be_numeric_strict")

        if type(self.value) is str:
            try:
                float(self.value)
                print(float(self.value))
                return True, assertion_text
            except Exception:
                pass
        return False, assertion_text

    def _internal_be_callable(self) -> Tuple[bool, str]:
        return callable(self.value), self._message("be_callable")

    @assertion
    def equal(self, something: Any) -> None:
        """Checks whether that the value is equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be(self, something: Any) -> None:
        """Checks whether the value is 'softly' equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def contain(self, something: Any) -> None:
        """Checks whether the value contains something

        Args:
            something (Any): The value to be contained

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_contained_in(self, something: Collection) -> None:
        """Checks whether the value is contained in something

        Args:
            something (Any): The value to contain something

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_empty(self) -> None:
        """Checks whether the value is empty

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_true(self) -> None:
        """Checks whether the value is true

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_false(self) -> None:
        """Checks whether the value is false

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_truthy(self) -> None:
        """Checks whether the value is truthy

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_falsey(self) -> None:
        """Checks whether the value is falsey

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_of_type(self, something: type) -> None:
        """Checks whether the value is of provided type

        Args:
            something (type): Type to be checked against

        Returns:
            bool: Result
        """
        pass

    @assertion
    def inherit(self, something: type) -> None:
        """Checks whether the value inherits from provided type

        Args:
            something (type): Type to inherit from

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_greater_than(self, something: Any) -> None:
        """Check whether the value is greater than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_lesser_than(self, something: Any) -> None:
        """Check whether the value is lesser than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_greater_or_equal_to(self, something: Any) -> None:
        """Check whether the value is greater than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_lesser_or_equal_to(self, something: Any) -> None:
        """Check whether the value is lesser than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_numeric(self, strict=False) -> None:
        """Check whether the value is numeric

        Returns:
            bool: Result
        """
        pass

    @assertion
    def be_callable(self) -> None:
        """Check whether the expected value is of type callable

        Returns:
            bool: Result
        """
        pass

    @hidetraceback
    def be_none(self) -> None:
        """Check whether the expected value is None

        Returns:
            bool: Result
        """
        return self.be(None)

    @hidetraceback
    def be_str(self) -> None:
        """Check whether the expected value is a string

        Returns:
            bool: Result
        """
        return self.be_of_type(str)

    @hidetraceback
    def be_bool(self) -> None:
        """Check whether the expected value is a bool

        Returns:
            bool: Result
        """
        return self.be_of_type(bool)

    @hidetraceback
    def be_int(self) -> None:
        """Check whether the expected value is an int

        Returns:
            bool: Result
        """
        return self.be_of_type(int)

    @hidetraceback
    def be_float(self) -> None:
        """Check whether the expected value is a float

        Returns:
            bool: Result
        """
        return self.be_of_type(float)

    @hidetraceback
    def be_list(self) -> None:
        """Check whether the expected value is a list

        Returns:
            bool: Result
        """
        return self.be_of_type(list)

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
