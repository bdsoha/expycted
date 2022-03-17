# Overview

__Expycted__ is yet another `expect` pattern implementation.

It is not dependent on any testing framework and can plug into any as it is just an abstraction over `assert`.

Examples:
```python
from expycted import expect

expect(True).to_not.be_false()                                  # This will succeed

expect([]).to.be_empty()                                        # This will succeed

expect([1,2,3]).to.contain(3)                                   # This will succeed

expect(10).to.equal("10")                                       # This will raise AssertionError

expect(10).to.be("10")                                          # This will succeed

expect.function(int).to_raise(ValueError).when_called_with('a') # This will also succeed

```

# Installation

__Expycted__ can be installed from PyPi by using:
```shell
pip install expycted
```

Alternatively, you can clone the repository and build your own distribution using poetry.
```sh
git clone https://github.com/petereon/expycted.git
poetry build
```
Then you can install it using:
```sh
pip install ./dist/expycted-<version>-py3-none-any.whl
```

# Matchers

Matchers are used to ensure some conditions are met.

## Value Matchers

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
    - `be_numeric(self)`: checks if `self.value` is a number or string covertible to a number. With alias `be_a_number`
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


## Function Matchers

Function matchers can be called as such:
```python
expect.function(string.replace).to_return('strength').when_called_with('ing', 'ength')
```

Currently available matchers are:
- `to_return(self, value=None, type_of_value=None)` - checks if function returns a specified value, or type, or both.
- `to_raise(self, exception_type)` - checks if function raises a specified exception.

In each case we have to specify arguments with which function is called in `.when_called_with` method. Method has aliases `when_called_with_args`, `when_called_with_arguments`

## Filesystem Matchers

Filesystem matchers can be called as such:
```python
expect.folder('/some/folder').to.contain('subfolder')
```
Currently available matchers are:
- `contain(self, name, type: Union[File, Folder, None, str] = None)` - checks if folder contains a specified file or folder. If type is specified, it will check if file is file or folder is folder.
- `contain_file(self, name)` - checks if folder contains a specified file.
- `contain_folder(self, name)` - checks if folder contains a specified folder.
- `exist(self)` - checks if folder exists.
- `be_empty(self)` - checks if folder is empty.

They can be used with both 'expect.folder('/some/folder').to' and 'expect.folder('/some/folder').to_not' to check both positive and negative expectations.