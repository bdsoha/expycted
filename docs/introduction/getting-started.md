# Getting Started

## Overview

**Expycted** uses expectations to allow you to test *actual values* against certain conditions or *expected values* matchers.
Expectations also allow you to write your tests like you would a humar-readable sentence:

### Example

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
