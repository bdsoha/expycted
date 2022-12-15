from __future__ import annotations

from typing import Any, Collection, Tuple
import pickle

from expycted.core.matchers import assertion
from expycted.internals.base import BaseExpectation
from expycted.internals.utils import assertion as assertion_old
from expycted.matchers import (
    BeEmptyMatcher,
    EqualMatcher,
    IsFalseMatcher,
    IsTrueMatcher,
    TypeMatcher,
)


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
            return issubclass(type(self.expected), actual), self._message(
                "inherit", actual
            )
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

    @property
    @assertion
    def equal(self) -> EqualMatcher:
        """Asserts that two variables have the same value."""

        return EqualMatcher

    @property
    def be_equal_to(self) -> EqualMatcher:
        """Alias for ``equal``."""

        return self.equal

    @assertion_old
    def be(self, actual: Any) -> None:
        """Checks whether the value is 'softly' equal to something

        Args:
            actual (Any): The value to compare to

        Returns:
            bool: Result
        """

    @assertion_old
    def contain(self, actual: Any) -> None:
        """Checks whether the value contains something

        Args:
            actual (Any): The value to be contained

        Returns:
            bool: Result
        """

    @assertion_old
    def be_contained_in(self, actual: Collection) -> None:
        """Checks whether the value is contained in something

        Args:
            actual (Any): The value to contain something

        Returns:
            bool: Result
        """

    @property
    @assertion
    def be_empty(self) -> BeEmptyMatcher:
        """Asserts that the actual value is empty."""

        return BeEmptyMatcher

    @property
    @assertion
    def be_true(self) -> IsTrueMatcher:
        """Asserts that the actual value is ``True``."""

        return IsTrueMatcher

    @property
    @assertion
    def be_false(self) -> IsFalseMatcher:
        """Asserts that the actual value is ``False``."""

        return IsFalseMatcher

    @property
    @assertion
    def be_truthy(self) -> IsTrueMatcher:
        """Asserts that the actual value is truthy."""

        return IsTrueMatcher(
            expectation=self.expected, negated=self.negate, strict=False
        )

    @property
    @assertion
    def be_trueish(self) -> IsTrueMatcher:
        """Alias for ``be_truthy``."""

        return self.be_truthy

    @property
    def be_truey(self) -> IsTrueMatcher:
        """Alias for ``be_truthy``."""

        return self.be_truthy

    @property
    @assertion
    def be_falsey(self) -> IsFalseMatcher:
        """Asserts that the actual value is falsey."""

        return IsFalseMatcher(
            expectation=self.expected, negated=self.negate, strict=False
        )

    @property
    def be_falsish(self) -> IsFalseMatcher:
        """Alias for ``be_falsey``."""

        return self.be_falsey

    @property
    def be_falsy(self) -> IsFalseMatcher:
        """Alias for ``be_falsey``."""

        return self.be_falsey

    @property
    @assertion
    def be_of_type(self) -> TypeMatcher:
        """Assert that the actual type is equivalent to the expected type."""

        return TypeMatcher

    @property
    def be_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

        return self.be_of_type

    @property
    def have_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

        return self.be_of_type

    @assertion_old
    def inherit(self, actual: type) -> None:
        """Checks whether the value inherits from provided type

        Args:
            actual (type): Type to inherit from

        Returns:
            bool: Result
        """

    @assertion_old
    def be_greater_than(self, actual: Any) -> None:
        """Check whether the value is greater than something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion_old
    def be_lesser_than(self, actual: Any) -> None:
        """Check whether the value is lesser than something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion_old
    def be_greater_or_equal_to(self, actual: Any) -> None:
        """Check whether the value is greater than or equal to something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion_old
    def be_lesser_or_equal_to(self, actual: Any) -> None:
        """Check whether the value is lesser than or equal to something

        Args:
            actual (Any): Value to compare to

        Returns:
            bool: Result
        """

    @assertion_old
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
