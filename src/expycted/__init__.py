
import pickle


class _To():

    def __init__(self, value):
        self.value = value

    def _has_len(self):
        try:
            len(self.value)
            return True
        except TypeError:
            return False


    def _equal(self, something):
        return self.value == something

    def _be(self, something):
        return any([
            str(self.value) == str(something),
            pickle.dumps(self.value) == pickle.dumps(something),
            self.value == something,
        ])

    def _contain(self, something):
        return something in self.value

    def _be_contained_in(self, something):
        return self.value in something

    def _be_empty(self):
        try:
            iter(self.value)
            return not self.value
        except TypeError:
            raise TypeError(
                f"Emptiness of '{type(self.value)}' object doesn't make sense")

    def _be_true(self):
        return self.value is True

    def _be_false(self):
        return self.value is False

    def _be_truthy(self):
        return self.value

    def _be_falsey(self):
        return not self.value

    def _be_of_type(self, something):
        return type(self.value) is something

    def _inherit(self, something):
        return issubclass(type(self.value), something)

    def _be_greater_than(self, something):
        return self.value > something

    def _be_lesser_than(self, something):
        return self.value < something

    def _be_greater_or_equal_to(self, something):
        return self.value >= something

    def _be_lesser_or_equal_to(self, something):
        return self.value <= something

    def _be_numeric(self):
        if type(self.value) in [int, float, complex]:
            return True
        elif type(self.value) is str:
            return all([i.isdigit() for i in self.value])


    def equal(self, something):
        assert self._equal(something)

    def be(self, something):
        assert self._be(something)

    def contain(self, something):
        assert self._contain(something)

    def be_contained_in(self, something):
        assert self._be_contained_in(something)

    def be_empty(self):
        assert self._be_empty()

    def be_true(self):
        assert self._be_true()

    def be_false(self):
        assert self._be_false()

    def be_truthy(self):
        assert self._be_truthy()

    def be_falsey(self):
        assert self._be_falsey()

    def be_of_type(self, something):
        assert self._be_of_type(something)

    def inherit(self, something):
        assert self._inherit(something)

    def be_greater_than(self, something):
        assert self._be_greater_than(something)

    def be_lesser_than(self, something):
        assert self._be_lesser_than(something)

    def be_greater_or_equal_to(self, something):
        assert self._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something):
        assert self._be_lesser_or_equal_to(something)

    def be_numeric(self):
        assert self._be_numeric()




class _ToNot(_To):

    def equal(self, something):
        assert not super()._equal(something)

    def be(self, something):
        assert not super()._be(something)

    def contain(self, something):
        assert not super()._contain(something)

    def be_contained_in(self, something):
        assert not super()._be_contained_in(something)

    def be_empty(self):
        assert not super()._be_empty()

    def be_true(self):
        assert not super()._be_true()

    def be_false(self):
        assert not super()._be_false()

    def be_truthy(self):
        assert not super()._be_truthy()

    def be_falsey(self):
        assert not super()._be_falsey()

    def be_of_type(self, something):
        assert not super()._be_of_type(something)

    def inherit(self, something):
        assert not super()._inherit(something)

    def be_greater_than(self, something):
        assert not super()._be_greater_than(something)

    def be_lesser_than(self, something):
        assert not super()._be_lesser_than(something)

    def be_greater_or_equal_to(self, something):
        assert not super()._be_greater_or_equal_to(something)

    def be_lesser_or_equal_to(self, something):
        assert not super()._be_lesser_or_equal_to(something)

    def be_numeric(self):
        assert not super()._be_numeric()


class _Expect:
    def __init__(self, value: None):
        self.to = _To(value)
        self.to_not = _ToNot(value)


def expect(something) -> _Expect:
    return _Expect(something)
