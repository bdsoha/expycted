from typing import Any, Collection, Tuple
import pickle

from expycted.core.matchers import assert_alias_property, assert_property
from expycted.internals.base import BaseExpectation
from expycted.internals.utils import assertion
from expycted.matchers import (
    BeEmptyMatcher,
    BoolMatcher,
    EqualMatcher,
    IsMatcher
)
from expycted.matchers.type_matcher import TypeMatcher


class Value(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "be": "Expected {expected} to be {actual}",
        "contain": "Expected {expected} to contain {actual}",
        "be_contained_in": "Expected {expected} to be contained in {actual}",
        "inherit": "Expected {expected} to inherit {actual}",
        "be_greater_than": "Expected {expected} to be greater than {actual}",
        "be_lesser_than": "Expected {expected} to be less than {actual}",
        "be_greater_or_equal_to": "Expected {expected} to be greater than or equal to {actual}",
        "be_lesser_or_equal_to": "Expected {expected} to be less than or equal to {actual}",
        "be_numeric": "Expected {expected} to be numeric",
    }

    def _internal_has_len(self: Any) -> bool:
        try:
            len(self.expected)
            return True
        except TypeError:
            return False

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

    @assert_property(EqualMatcher)
    def equal(self) -> EqualMatcher:
        """Asserts that two variables have the same value."""

    @assert_alias_property("equal")
    def be_equal_to(self) -> EqualMatcher:
        """Alias for ``equal``."""

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

    @assert_property(BeEmptyMatcher)
    def be_empty(self) -> BeEmptyMatcher:
        """Asserts that the actual value is empty."""

    @assert_property(IsMatcher, to_match=True)
    def be_true(self) -> IsMatcher:
        """Asserts that the actual value is ``True``."""

    @assert_property(IsMatcher, to_match=False)
    def be_false(self) -> IsMatcher:
        """Asserts that the actual value is ``False``."""

    @assert_property(BoolMatcher, to_match=True)
    def be_truthy(self) -> BoolMatcher:
        """Asserts that the actual value is truthy."""

    @assert_alias_property("be_truthy")
    def be_trueish(self) -> BoolMatcher:
        """Alias for ``be_truthy``."""

    @assert_alias_property("be_truthy")
    def be_truey(self) -> BoolMatcher:
        """Alias for ``be_truthy``."""

    @assert_property(BoolMatcher, to_match=False)
    def be_falsey(self) -> BoolMatcher:
        """Asserts that the actual value is falsey."""

    @assert_alias_property("be_falsey")
    def be_falsish(self) -> BoolMatcher:
        """Alias for ``be_falsey``."""

    @assert_alias_property("be_falsey")
    def be_falsy(self) -> BoolMatcher:
        """Alias for ``be_falsey``."""

    @assert_property(TypeMatcher)
    def be_of_type(self) -> TypeMatcher:
        """Assert that the actual type is equivelent to the expected type."""

    @assert_alias_property("be_of_type")
    def be_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

    @assert_alias_property("be_of_type")
    def have_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

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

    # Aliases

    be_a_number = be_numeric

    be_lesser = be_less = be_less_than = be_lesser_than
    be_lesser_or_equal = (
        be_less_or_equal
    ) = be_less_than_or_equal_to = be_lesser_than_or_equal_to = be_lesser_or_equal_to

    be_greater_or_equal = be_greater_than_or_equal_to = be_greater_or_equal_to
    be_greater = be_greater_than

    be_in = be_included_in = be_contained_in
    have = include = contain

    be_subclass_of = have_parent = inherit
