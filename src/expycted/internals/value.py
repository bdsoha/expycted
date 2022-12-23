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
    LessThanMatcher,
    GreatThanMatcher,
    TypeMatcher,
)


class Value(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "be": "Expected {expected} to be {actual}",
        "contain": "Expected {expected} to contain {actual}",
        "be_contained_in": "Expected {expected} to be contained in {actual}",
        "inherit": "Expected {expected} to inherit {actual}",
        "be_greater_than": "Expected {expected} to be greater than {actual}",
        "be_greater_or_equal_to": "Expected {expected} to be greater than or equal to {actual}",
        "be_numeric": "Expected {expected} to be numeric",
    }

    def _internal_be(self, actual: Any) -> Tuple[bool, str]:
        return any(
            [
                str(self._actual) == str(actual),
                pickle.dumps(self._actual) == pickle.dumps(actual),
                self._actual == actual,
            ]
        ), self._message("be", actual)

    def _internal_contain(self, expected: Any) -> Tuple[bool, str]:
        try:
            return expected in self._actual, self._message("contain", expected)
        except Exception:
            raise AssertionError(
                f'Type "{type(self._actual)} cannot contain {expected}"'
            )

    def _internal_be_contained_in(self, expected: Collection) -> Tuple[bool, str]:
        try:
            return self._actual in expected, self._message("be_contained_in", expected)
        except Exception:
            raise AssertionError(
                f'Type "{type(expected)} cannot contain {self._actual}"'
            )

    def _internal_inherit(self, expected: type) -> Tuple[bool, str]:
        try:
            return issubclass(type(self._actual), expected), self._message(
                "inherit", expected
            )
        except Exception:
            raise AssertionError("Second argument must be a class, not an instance")

    def _internal_be_greater_than(self, expected: Any) -> Tuple[bool, str]:
        return self._actual > expected, self._message("be_greater_than", expected)

    def _internal_be_greater_or_equal_to(self, expected: Any) -> Tuple[bool, str]:
        return self._actual >= expected, self._message(
            "be_greater_or_equal_to", expected
        )

    def _internal_be_numeric(self: Any) -> Tuple[bool, str]:
        assertion_text = self._message("be_numeric")

        if type(self._actual) in [int, float, complex]:
            return True, assertion_text

        if type(self._actual) is str:
            try:
                float(self._actual)
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

        return IsTrueMatcher(self, strict=False)

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

        return IsFalseMatcher(self, strict=False)

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

    @property
    @assertion
    def be_greater_than(self) -> GreatThanMatcher:
        """Asserts that the actual value is greater than the expected value."""

        return GreatThanMatcher

    @property
    @assertion
    def be_greater_than_or_equal_to(self) -> GreatThanMatcher:
        """Asserts that the actual value is greater than or equal to the expected value."""

        return GreatThanMatcher(self, or_equal=True)

    @property
    def be_great_than(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than``."""

        return self.be_greater_than

    @property
    def be_great(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than``."""

        return self.be_greater_than

    @property
    def be_greater(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than``."""

        return self.be_greater_than

    @property
    def be_greater_or_equal_to(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    def be_great_than_or_equal_to(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    def be_great_or_equal(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    def be_greater_or_equal(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    @assertion
    def be_lesser_than(self) -> LessThanMatcher:
        """Asserts that the actual value is lesser than the expected value."""

        return LessThanMatcher

    @property
    @assertion
    def be_lesser_than_or_equal_to(self) -> LessThanMatcher:
        """Asserts that the actual value is lesser than or equal to the expected value."""

        return LessThanMatcher(self, or_equal=True)

    @property
    def be_less_than(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_less(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_lesser(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_lesser_or_equal_to(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_less_than_or_equal_to(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_less_or_equal(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_lesser_or_equal(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @assertion_old
    def be_numeric(self) -> None:
        """Check whether the value is numeric

        Returns:
            bool: Result
        """

    # Aliases

    be_a_number = be_numeric

    be_in = be_included_in = be_contained_in
    have = include = contain

    be_subclass_of = have_parent = inherit
