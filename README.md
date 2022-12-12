# Expycted

[![Build and Test Python Package](https://github.com/bdsoha/expycted/actions/workflows/python-package.yml/badge.svg)](https://github.com/petereon/expycted/actions/workflows/python-package.yml)

__Table of Contents__

- [Overview](#overview)
- [Installation](#installation)
- [Matchers](#matchers)
    - [Value Matchers](#value-matchers)
    - [Function Matchers](#function-matchers)
    - [Filesystem Matchers](#filesystem-matchers)
- [Development](#development)
- [Contributing](#contributing)

## Overview

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

**This package was originally written by @petereon, many thanks!**

## Installation

__Expycted__ can be installed from [PyPi](https://pypi.org/project/expycted/) by running:
```sh
pip install expycted
```

Alternatively, you can clone the repository and build your own distribution using poetry:
```sh
git clone https://github.com/bdsoha/expycted.git
poetry build
```
Then you can install it using:
```sh
pip install ./dist/expycted-<version>-py3-none-any.whl
```

## Matchers

Matchers are used to ensure some conditions are met on an *expected* value.

## Value Matchers

Value matchers can be used in two equivalent ways demonstrated below:

```python
expect.value(10).to.be_greater_than(1)
expect(10).to.be_greater_than(1)
```

Currently available matchers are:

### Equality and Similarity

#### equal()
Assert that the *expected* value is equivalent to the *actual* value using the `==` operator.
- __Definition:__ `equal(self, value)`
- __Alias:__ `be_equal_to(self, value)`

#### be()
Assert that the *expected* value is the same as the *actual* value.
- __Definition:__ `be(self, value)`
- __Details:__ Assert any of the following conditions:
    - Assert the *expected* value's string representation is the same as the *actual* value's string representation.
    - When provided two objects, assert that have the same attributes.
    - Assert the *expected* value equals the *actual* value.

### Numeric

#### be_greater_than()
Assert that the *expected* value is greater than the *actual* value using the `>` operator.
- __Definition:__ `be_greater_than(self, value)`
- __Alias:__ `be_greater(self, value)`

#### be_lesser_than()
Assert that the *expected* value is less than the *actual* value using the `<` operator.
- __Definition:__ `be_lesser_than(self, value)`
- __Alias:__
    - `be_lesser(self, value)`
    - `be_less(self, value)`
    - `be_less_than(self, value)`

#### be_greater_or_equal_to()
Assert that the *expected* value is greater than the *actual* value using the `>=` operator.
- __Definition:__ `be_greater_or_equal_to(self, value)`
- __Alias:__
    - `be_greater_or_equal(self, value)`
    - `be_greater_than_or_equal_to(self, value)`

#### be_lesser_or_equal_to()
Assert that the *expected* value is less than the *actual* value using the `<=` operator.
- __Definition:__ `be_lesser_or_equal_to(self, value)`
- __Alias:__
    - `be_lesser_or_equal(self, value)`
    - `be_less_or_equal(self, value)`
    - `be_less_than_or_equal_to(self, value)`
    - `be_lesser_than_or_equal_to(self, value)`

#### be_numeric()
Assert that the *expected* value is a number or can be parsed as a number from a string representation.
- __Definition:__ `be_numeric(self)`
- __Alias:__ `be_a_number(self)`


### Containment and Emptiness

#### contain()
Assert the *expected* value contains a value using the `in` keyword.
- __Definition:__ `contain(self, value)`
- __Alias:__
    - `have(self, value)`
    - `include(self, value)`

#### be_contained_in()
Assert the *expected* value is contained in a value using the `in` keyword.
- __Definition:__ `be_contained_in(self, value)`
- __Alias:__
    - `be_in(self, value)`
    - `be_included_in(self, value)`

#### be_empty()
Assert that the *expected* value is `iterable` and `False`.
- __Definition:__ `be_empty(self)`

### Truthiness

#### be_true()
Assert that the *expected* value is strictly `True`.
- __Definition:__ `be_true(self)`

#### be_false()
Assert that the *expected* value is strictly `False`.
- __Definition:__ `be_false(self)`

#### be_truthy()
Assert that the *expected* value is equivalent to `True`.
- __Definition:__ `be_truthy(self)`
- __Alias:__
    - `be_truey(self)`
    - `be_trueish(self)`

#### be_falsey()
Assert that the *expected* value is equivalent to `False`.
- __Definition:__ `be_falsey(self)`
- __Alias:__
    - `be_falsy(self)`
    - `be_falsish(self)`

### Typing

#### be_of_type()
Assert that the *expected* value has a given type.
- __Definition:__ `be_of_type(self, value)`
- __Alias:__
    - `be_type(self, value)`
    - `have_type(self, value)`

#### inherit()
Assert that the *expected* value inherits or is a subclass of a given type.
- __Definition:__ `inherit(self, value)`
- __Alias:__
    - `be_subclass_of(self, value)`
    - `have_parent(self, value)`

## Function Matchers

Function matchers can be used as demonstrated below:
```python
expect.function(string.replace).to_return('strength').when_called_with('string', 'ength')
```

Arguments can be passed to the *expected* function using the `.when_called_with` method, *(or its alias methods: `when_called_with_args` and `when_called_with_arguments`)*.

#### to_return()
Assert that the *expected* function returns the *actual* value, or type, or both.
- __Definition:__ `to_return(self, value=None, type_of_value=None)`

#### to_raise()
Assert that the *expected* function raises the *actual* exception of a given type.
- __Definition:__ `to_raise(self, exception_type)`


## Filesystem Matchers

Filesystem matchers can be used as demonstrated below:
```python
expect.folder('/some/folder').to.contain('subfolder')
```

Matchers can be used with both `expect.folder('/some/folder').to` and `expect.folder('/some/folder').to_not` to check both positive and negative expectations.

#### contain()
Assert that the *expected* folder contains the *actual* file or folder.
- __Definition:__ `contain(self, name, type: Union[File, Folder, None, str] = None)`
- __Details:__ When the `type` argument is specified, it will also assert whether *actual* value is a `File` or `Folder`.

#### contain_file()
Assert that the *expected* folder contains the *actual* file.
- __Definition:__ `contain_file(self, name)`

#### contain_folder()
Assert that the *expected* folder contains the *actual* folder.
- __Definition:__ `contain_folder(self, name)`

#### exist()
Assert that the *expected* folder exists.
- __Definition:__ `exist(self)`

#### be_empty()
Assert that the *expected* folder is empty.
- __Definition:__ `be_empty(self)`


## Development

For development a combination of `poetry` and `pipenv` is used. `pipenv` is used to install dependencies and manage virtual environments while `poetry` is used for building and metadata management.

To begin developing run the following commands in your terminal:
```sh
# Clone the repository
git clone https://github.com/bdsoha/expycted.git

# Install dependencies
pipenv install

# Run tests
pipenv run test

# Build the package
pipenv run build
```

## Contributing

__Project is currently in its infancy, contributors, pull requests and issues are welcome__
