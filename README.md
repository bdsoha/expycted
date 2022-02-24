# Expycted

:no_good: :no_good: __WARNING: LIBRARY IS CURRENTY UNTESTED__ :no_good: :no_good:

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

- `equal`
- `be`
- `contain`
- `be_contained_in`
- `be_empty`
- `be_true`
- `be_false`
- `be_truthy`
- `be_falsey`
- `be_of_type`

:building_construction: __Note__: Numeric matchers are in-progress :building_construction:

__Project is currently in its infancy, contributors and issues are welcome__
