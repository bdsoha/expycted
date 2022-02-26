# Expycted

Yet another `expect` pattern implementation.

Expycted is not dependent on any testing framework and can plug into any as it is just an abstraction over `assert`.

Examples:
```python
from expycted import expect

expect(True).to_not.be_false()                                                              # This will succeed

expect([]).to.be_empty()                                                                    # This will succeed

expect([1,2,3]).to.contain(3)                                                               # This will succeed

expect(10).to.equal("10")                                                                   # This will raise AssertionError

expect(10).to.be("10")                                                                      # This will succeed

expect.function('string'.replace).to_return('strength').when_called_with('ing', 'ength')    # This will succeed

expect.function(int).to_raise(ValueError).when_called_with('a')                             # This will also succeed

```

## Matchers

Matchers are used to ensure some conditions are met.

### Value Matchers

Value matchers can be used in two equivalent ways demonstrated below:

```python
expect.value(10).to.be_greater_than(1)
expect(10).to.be_greater_than(1)
```

Currently available matchers are:

- Eqality and similarity
    - `equal(self, value)`: equivalent to "`==`". With alias `be_equal_to`
    - `be(self, value)`:  will check if string representation of values is same or if two objects have the same attributes or are equal
- Numeric
    - `be_greater_than(self, value)`: equivalent to "`>`". With alias `be_greater`
    - `be_lesser_than(self, value)`: equivalent to "`<`". With alias `be_lesser `, `be_less`, `be_less_than`
    - `be_greater_or_equal_to(self, value)`: equivalent to "`>=`". With aliases `be_greater_or_equal`, `be_greater_than_or_equal_to`
    - `be_lesser_or_equal_to(self, value)`: equivalent to "`<=`". With aliases `be_lesser_or_equal`, `be_less_or_equal`, `be_less_than_or_equal_to`, `be_lesser_than_or_equal_to`
    - `is_numeric(self)`: checks if `self.value` is a number or string covertible to a number. With alias `be_a_number`
- Containment and Emptiness
    - `contain(self, value)`: equivalent to "`in`". With aliases `have`, `include`
    - `be_contained_in(self, value)`: equivalent to "`in`". Qith aliases `be_in`, `be_included_in`
    - `be_empty(self)`: checks if `self.value` is iterable and `False`
- Truthiness
    - `be_true(self)`: checks if `self.value` is `True`
    - `be_false(self)`: checks if `self.value` is `False`
    - `be_truthy(self)`: checks if `self.value` behaves _true_ in if statement. With aliases `be_truey`, `be_trueish `
    - `be_falsey(self)`: checks if `self.value` behaves _false_ in if statement. With aliases `be_falsy`, `be_falsish`
- Typing
    - `be_of_type(self, value)`: checks if `self.value` is of specified type. With aliases `be_type`, `have_type`
    - `inherit(self, value)`: checks if `self.value` inherits/is a specified type. `be_subclass_of`, `have_parent`


### Function Matchers

Function matchers can be called as such:
```python
expect.function(string.replace).to_return('strength').when_called_with('ing', 'ength')
```

Currently available matchers are:
- `to_return(self, value=None, type_of_value=None)` - checks if function returns a specified value, or type, or both.
- `to_raise(self, exception_type)` - checks if function raises a specified exception.

In each case we have to specify arguments with which function is called in `.when_called_with` method. Method has aliases `when_called_with_args`, `when_called_with_arguments`

__Project is currently in its infancy, contributors, pull requests and issues are welcome__
