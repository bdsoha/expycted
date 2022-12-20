# Getting Started

## Overview

**Expycted** uses expectations to allow you to test *actual values* against certain conditions or *expected values* matchers.
Expectations also allow you to write your tests like you would a humar-readable sentence.

## Expectations

This document will provide a brief introduction the concept of Expectations. For the full list of expectations, see the [`expect` documentation →](/expectations/interface/main).

Let's start with a simple example of testing that an actual value is equal to an expected value.

```python
from expycted import expect

def test():
  expect("hello" + " " + "world").to.equal("hello world")
```

The code above, `expect("hello" + " " + "world")` returns an `Expectation` object. You typically won't directly interact with the expectation objects, instead, you will *chain* calls to matchers on them. The `.to` property above, is [one of many chainable getters](/expectations/interface/chains), made to improve the readability of your assertions. The `.equal("hello world")` is the matcher and behind the scenes uses the `==` to test for equality.

### More Examples

```python
from expycted import expect

def test_1():
  expect(True).to_not.be_false()

def test_2():
  expect([]).to.be_empty()

def test_3():
  expect([1, 2, 3]).to.contain(3)

def test_4():
  # This will raise `AssertionError`
  expect(10).to.equal("10")

def test_5():
  expect(10).to.be("10")
```
