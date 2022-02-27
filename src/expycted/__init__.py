import pickle
from typing import Any, Collection


class _To():
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
        assert self._equal(something)

    def be(self, something: Any) -> bool:
        assert self._be(something)

    def contain(self, something: Any) -> bool:
        assert self._contain(something)

    def be_contained_in(self, something: Collection) -> bool:
        assert self._be_contained_in(something)

    def be_empty(self) -> bool:
        assert self._be_empty()

    def be_true(self) -> bool:
        assert self._be_true()

    def be_false(self) -> bool:
        assert self._be_false()

    def be_truthy(self) -> bool:
        assert self._be_truthy()

    def be_falsey(self) -> bool:
        assert self._be_falsey()

    def be_of_type(self, something: type) -> bool:
        assert self._be_of_type(something)

    def inherit(self, something: type) -> bool:
        assert self._inherit(something)

    def be_greater_than(self, something: Any) -> bool:
        assert self._be_greater_than(something)

    def be_lesser_than(self, something: Any) -> bool:
        assert self._be_lesser_than(something)

    def be_greater_or_equal_to(self, something: Any) -> bool:
        assert self._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something: Any) -> bool:
        assert self._be_lesser_or_equal_to(something)

    def be_numeric(self) -> bool:
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


class _ToNot(_To):
    value: Any

    def equal(self, something: Any) -> bool:
        assert not super()._equal(something)

    def be(self, something: Any) -> bool:
        assert not super()._be(something)

    def contain(self, something: Any) -> bool:
        assert not super()._contain(something)

    def be_contained_in(self, something: Collection) -> bool:
        assert not super()._be_contained_in(something)

    def be_empty(self) -> bool:
        assert not super()._be_empty()

    def be_true(self) -> bool:
        assert not super()._be_true()

    def be_false(self) -> bool:
        assert not super()._be_false()

    def be_truthy(self) -> bool:
        assert not super()._be_truthy()

    def be_falsey(self) -> bool:
        assert not super()._be_falsey()

    def be_of_type(self, something: type) -> bool:
        assert not super()._be_of_type(something)

    def inherit(self, something: type) -> bool:
        assert not super()._inherit(something)

    def be_greater_than(self, something: Any) -> bool:
        assert not super()._be_greater_than(something)

    def be_lesser_than(self, something: Any) -> bool:
        assert not super()._be_lesser_than(something)

    def be_greater_or_equal_to(self, something) -> bool:
        assert not super()._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something: Any) -> bool:
        assert not super()._be_lesser_or_equal_to(something)

    def be_numeric(self) -> bool:
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


class _Function:
    def __init__(self, function: callable):
        self.function = function

    def to_raise(self, exception: Exception):
        return _ToRaise(exception=exception, function=self.function)

    def to_return(self, value: Any = None, type_of_value: type = None):
        if value is None and type_of_value is None:
            raise AssertionError(
                'You must specify either value or type_of_value in to_return function')
        else:
            return _ToReturn(value=value, type_of_value=type_of_value, function=self.function)


class _ToRaise:
    function: callable
    exception: Exception

    def __init__(self, exception: Exception, function: callable):
        self.function = function
        self.exception = exception

    def when_called_with(self, *args, **kwargs):
        try:
            self.function(*args, **kwargs)
        except Exception as e:
            print(e)
            print(self.exception)
            assert type(e) == self.exception
        else:
            raise AssertionError(
                f"Expected '{self.exception}' to be raised, but nothing was raised")

    when_called_with_args = when_called_with_arguments = when_called_with


class _ToReturn:
    function: callable
    value: Any
    type_of_value: type

    def __init__(self, function: callable, value, type_of_value):
        self.function = function
        self.value = value
        self.type_of_value = type_of_value

    def when_called_with(self, *args, **kwargs):
        ret = self.function(*args, **kwargs)
        if self.value is not None:
            assert ret == self.value
        if self.type_of_value is not None:
            assert type(ret) == self.type_of_value

    when_called_with_args = when_called_with_arguments = when_called_with


class expect:
    def __init__(self, value: any):
        self.to = _To(value)
        self.to_not = _ToNot(value)

    @staticmethod
    def function(function: callable):
        return _Function(function)

    @staticmethod
    def value(value: any):
        return expect(value)
