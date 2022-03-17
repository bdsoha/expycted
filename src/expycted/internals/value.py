import pickle
from typing import Any, Collection

class To:
    value: Any

    def __init__(self, value):
        self.value = value

    def _has_len(self: Any) -> bool:
        try:
            len(self.value)
            return True
        except TypeError:
            return False

    def _equal(self, something: Any) -> bool:
        return self.value == something

    def _be(self, something: Any) -> bool:
        return any([
            str(self.value) == str(something),
            pickle.dumps(self.value) == pickle.dumps(something),
            self.value == something,
        ])

    def _contain(self, something: Any) -> bool:
        try:
            return something in self.value
        except Exception:
            raise AssertionError(
                f'Type "{type(self.value)} cannot contain {something}"')

    def _be_contained_in(self, something: Collection) -> bool:
        try:
            return self.value in something
        except Exception:
            raise AssertionError(
                f'Type "{type(something)} cannot contain {self.value}"')

    def _be_empty(self):
        try:
            iter(self.value)
            return not self.value
        except TypeError:
            raise AssertionError(
                f"Emptiness of '{type(self.value)}' object doesn't make sense")

    def _be_true(self) -> bool:
        return self.value is True

    def _be_false(self) -> bool:
        return self.value is False

    def _be_truthy(self) -> bool:
        return True if self.value else False

    def _be_falsey(self) -> bool:
        return True if not self.value else False

    def _be_of_type(self, something: type) -> bool:
        return type(self.value) is something

    def _inherit(self, something: type) -> bool:
        try:
            return issubclass(type(self.value), something)
        except Exception:
            raise AssertionError(
                'Second argument must be a class, not an instance')

    def _be_greater_than(self, something: Any) -> bool:
        return self.value > something

    def _be_lesser_than(self, something: Any) -> bool:
        return self.value < something

    def _be_greater_or_equal_to(self, something: Any) -> bool:
        return self.value >= something

    def _be_lesser_or_equal_to(self, something: Any) -> bool:
        return self.value <= something

    def _be_numeric(self: Any) -> bool:
        if type(self.value) in [int, float, complex]:
            return True
        elif type(self.value) is str:

            try:
                float(self.value)
                return True
            except Exception:
                return False

    def equal(self, something: Any) -> bool:
        """Checks whether that the value is equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        assert self._equal(something)

    def be(self, something: Any) -> bool:
        """Checks whether the value is 'softly' equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        assert self._be(something)

    def contain(self, something: Any) -> bool:
        """Checks whether the value contains something

        Args:
            something (Any): The value to be contained

        Returns:
            bool: Result
        """
        assert self._contain(something)

    def be_contained_in(self, something: Collection) -> bool:
        """Checks whether the value is contained in something

        Args:
            something (Any): The value to contain something

        Returns:
            bool: Result
        """
        assert self._be_contained_in(something)

    def be_empty(self) -> bool:
        """Checks whether the value is empty

        Returns:
            bool: Result
        """
        assert self._be_empty()

    def be_true(self) -> bool:
        """Checks whether the value is true

        Returns:
            bool: Result
        """
        assert self._be_true()

    def be_false(self) -> bool:
        """Checks whether the value is false

        Returns:
            bool: Result
        """
        assert self._be_false()

    def be_truthy(self) -> bool:
        """Checks whether the value is truthy

        Returns:
            bool: Result
        """
        assert self._be_truthy()

    def be_falsey(self) -> bool:
        """Checks whether the value is falsey

        Returns:
            bool: Result
        """
        assert self._be_falsey()

    def be_of_type(self, something: type) -> bool:
        """Checks whether the value is of provided type

        Args:
            something (type): Type to be checked against

        Returns:
            bool: Result
        """
        assert self._be_of_type(something)

    def inherit(self, something: type) -> bool:
        """Checks whether the value inherits from provided type

        Args:
            something (type): Type to inherit from

        Returns:
            bool: Result
        """
        assert self._inherit(something)

    def be_greater_than(self, something: Any) -> bool:
        """Check whether the value is greater than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert self._be_greater_than(something)

    def be_lesser_than(self, something: Any) -> bool:
        """Check whether the value is lesser than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert self._be_lesser_than(something)

    def be_greater_or_equal_to(self, something: Any) -> bool:
        """Check whether the value is greater than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert self._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something: Any) -> bool:
        """Check whether the value is lesser than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert self._be_lesser_or_equal_to(something)

    def be_numeric(self) -> bool:
        """Check whether the value is numeric

        Returns:
            bool: Result
        """
        assert self._be_numeric()

    # Aliases

    be_a_number = be_numeric

    be_lesser = be_less = be_less_than = be_lesser_than
    be_lesser_or_equal = be_less_or_equal = be_less_than_or_equal_to = be_lesser_than_or_equal_to = be_lesser_or_equal_to

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

    def equal(self, something: Any) -> bool:
        """Checks whether that the value is not equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        assert not super()._equal(something)

    def be(self, something: Any) -> bool:
        """Checks whether the value is not 'softly' equal to something

        Args:
            something (Any): The value to compare to

        Returns:
            bool: Result
        """
        assert not super()._be(something)

    def contain(self, something: Any) -> bool:
        """Checks whether the value does not contains something

        Args:
            something (Any): The value to be contained

        Returns:
            bool: Result
        """
        assert not super()._contain(something)

    def be_contained_in(self, something: Collection) -> bool:
        """Checks whether the value is not contained in something

        Args:
            something (Any): The value to contain something

        Returns:
            bool: Result
        """
        assert not super()._be_contained_in(something)

    def be_empty(self) -> bool:
        """Checks whether the value is not empty

        Returns:
            bool: Result
        """
        assert not super()._be_empty()

    def be_true(self) -> bool:
        """Checks whether the value is not true

        Returns:
            bool: Result
        """
        assert not super()._be_true()

    def be_false(self) -> bool:
        """Checks whether the value is not false

        Returns:
            bool: Result
        """
        assert not super()._be_false()

    def be_truthy(self) -> bool:
        """Checks whether the value is not truthy

        Returns:
            bool: Result
        """
        assert not super()._be_truthy()

    def be_falsey(self) -> bool:
        """Checks whether the value is not falsey

        Returns:
            bool: Result
        """
        assert not super()._be_falsey()

    def be_of_type(self, something: type) -> bool:
        """Checks whether the value is not of provided type

        Args:
            something (type): Type to be checked against

        Returns:
            bool: Result
        """
        assert not super()._be_of_type(something)

    def inherit(self, something: type) -> bool:
        """Checks whether the value does not inherits from provided type

        Args:
            something (type): Type to inherit from

        Returns:
            bool: Result
        """
        assert not super()._inherit(something)

    def be_greater_than(self, something: Any) -> bool:
        """Check whether the value is not greater than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert not super()._be_greater_than(something)

    def be_lesser_than(self, something: Any) -> bool:
        """Check whether the value is not lesser than something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert not super()._be_lesser_than(something)

    def be_greater_or_equal_to(self, something) -> bool:
        """Check whether the value is not greater than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert not super()._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something: Any) -> bool:
        """Check whether the value is not lesser than or equal to something

        Args:
            something (Any): Value to compare to

        Returns:
            bool: Result
        """
        assert not super()._be_lesser_or_equal_to(something)

    def be_numeric(self) -> bool:
        """Check whether the value is not numeric

        Returns:
            bool: Result
        """
        assert not super()._be_numeric()

    # Aliases

    be_a_number = be_numeric

    be_lesser = be_less = be_less_than = be_lesser_than
    be_lesser_or_equal = be_less_or_equal = be_less_than_or_equal_to = be_lesser_than_or_equal_to = be_lesser_or_equal_to

    be_greater_or_equal = be_greater_than_or_equal_to = be_greater_or_equal_to
    be_greater = be_greater_than

    be_falsy = be_falsish = be_falsey
    be_truey = be_trueish = be_truthy

    be_in = be_included_in = be_contained_in
    have = include = contain

    be_equal_to = equal
    be_type = have_type = be_of_type
    be_subclass_of = have_parent = inherit