# Getting Started

## Overview

**Expycted** is yet another `expect` pattern implementation with rich and human-readable assertions.
It has no external dependencies and is not reliant on any specific testing framework.
You can use it project-wide or choose to slowely integrate it alongside existing `assert` calls, it is completely opt-in.

## Example

```python
from expycted import expect

# This will succeed
expect(True).to_not.be_false()                                  

# This will succeed
expect([]).to.be_empty()                                        

# This will succeed
expect([1, 2, 3]).to.contain(3)                                   

# This will raise AssertionError
expect(10).to.equal("10")                                       

# This will succeed
expect(10).to.be("10")                                          

# This will also succeed
expect.function(int).to_raise(ValueError).when_called_with("a") 
```
