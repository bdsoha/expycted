from __future__ import annotations

from typing import Any, Callable, NamedTuple

from pytest_lazyfixture import lazy_fixture
import pytest

from expycted import expect
from expycted.core.exceptions import MatcherError


class Context(NamedTuple):
    raises = pytest.raises(AssertionError)
    type_error = pytest.raises(MatcherError)


class DescribedParam(NamedTuple):
    value: Any
    description: str

    def __call__(self, *args, **kwargs):
        return self


class ExpectationParam(NamedTuple):
    actual_: Any = None
    expected_: Any = None
    description_: str = ""
    matcher_: Callable = None

    @property
    def actual(self):
        if isinstance(self.actual_, DescribedParam):
            return self.actual_.value

        return self.actual_

    @property
    def expected(self):
        if isinstance(self.expected_, DescribedParam):
            return self.expected_.value

        return self.expected_

    @property
    def description(self):
        if self.description_:
            return self.description_

        description = []

        if isinstance(self.expected_, DescribedParam):
            description.append(self.expected_.description)

        if isinstance(self.actual_, DescribedParam):
            description.append(self.actual_.description)

        return " -- ".join(description)

    def __str__(self):
        return self.description

    def matcher(self, **kwargs):
        return self.matcher_(self.actual, **kwargs)  # pylint: disable=not-callable

    @classmethod
    def create(cls, item, matcher, wrap):
        if wrap:
            item = (item,)

        return cls(
            actual_=item[0],
            expected_=item[1] if len(item) > 1 else None,
            description_=item[2] if len(item) > 2 else None,
            matcher_=matcher if matcher else expect,
        )


def expected_params(params, argnames="expected", extract_ids=True, **kwargs):
    if extract_ids:
        kwargs["ids"] = tuple(map(lambda i: i[-1], params))
        params = tuple(map(lambda i: i[:-1], params))

    return pytest.mark.parametrize(argnames, argvalues=params, **kwargs)


def expected_actual_params(params, argnames="expected,actual", **kwargs):
    return expected_params(params, argnames, **kwargs)


def parametrize_expectation(
    argvalues,
    argnames="expectation",
    matcher: Callable = None,
    wrap=True,
    **kwargs,
):
    argvalues = map(
        lambda i: ExpectationParam.create(i, matcher, wrap),
        argvalues,
    )

    argvalues = tuple(argvalues)

    return pytest.mark.parametrize(
        argnames=argnames,
        argvalues=argvalues,
        ids=str,
        **kwargs,
    )
