# Getting Started

## Overview

**Expycted** is yet another `expect` pattern implementation with rich and human-readable assertions.

It is not dependent on any testing framework and can plug into any existing framework.

## Example

```python
from expycted import expect

# This will succeed
expect(True).to_not.be_false()                                  

# This will succeed
expect([]).to.be_empty()                                        

# This will succeed
expect([1,2,3]).to.contain(3)                                   

# This will raise AssertionError
expect(10).to.equal("10")                                       

# This will succeed
expect(10).to.be("10")                                          

# This will also succeed
expect.function(int).to_raise(ValueError).when_called_with("a") 
```