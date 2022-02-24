# Expycted

I wished my Python tests were more readable. Now yours can be too. :mag: :mag:

Examples:
```python
expect(True).to_not.be_false()    # This will succeed

expect([]).to.be_empty()          # This will succeed

expect([1,2,3]).to.contain(3)     # This will succeed

expect(10).to.equal("10")         # This will raise AssertionError

expect(10).to.be("10")            # This will succeed

```

Currently available matchers are:

- Eqality and similarity
    - `equal(self, value)`: equivalent to "`==`"
    - `be(self, value)`:  will check if string representation of values is same or if two objects have the same attributes or are equal
- Numeric
    - `be_greater_than(self, value)`: equivalent to "`>`"
    - `be_lesser_than(self, value)`: equivalent to "`<`"
    - `be_greater_or_equal_to(self, value)`: equivalent to "`>=`"
    - `be_lesser_or_equal_to(self, value)`: equivalent to "`<=`"
    - `is_numeric(self)`: checks if `self.value` is a number or string covertible to a number
- Containment and Emptiness
    - `contain(self, value)`: equivalent to "`in`"
    - `be_contained_in(self, value)`: equivalent to "`in`"
    - `be_empty(self)`: checks if `self.value` is iterable and `False`
- Truthiness
    - `be_true(self)`: checks if `self.value` is `True`
    - `be_false(self)`: checks if `self.value` is `False`
    - `be_truthy(self)`: checks if `self.value` behaves _true_ in if statement
    - `be_falsey(self)`: checks if `self.value` behaves _false_ in if statement
- Typing
    - `be_of_type(self, value)`: checks if `self.value` is of specified type
    - `inherit(self, value)`: checks if `self.value` inherits/is a specified type

__Project is currently in its infancy, contributors and issues are welcome__
