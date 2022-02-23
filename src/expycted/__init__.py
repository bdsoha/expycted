
class To():
    
    def __init__(self, value):
        self.value = value
    
    def _equal(self, something):
        return self.value == something
    
    def _be(self, something):
        return str(self.value) == str(something)
    
    def _contain(self, something):
        return something in self.value
    
    def _be_contained_in(self, something):
        return self.value in something
    
    def _be_empty(self):
        try:
            iter(self.value)
            return not self.value
        except TypeError:
            raise TypeError(f"Emptiness of '{type(self.value)}' object doesn't make sense")

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


class ToNot(To):
    
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
    

class Expect:
    def __init__(self, value: None):
        self.to = To(value)
        self.to_not = ToNot(value)
    
    
def expect(something) -> Expect:
    return Expect(something)