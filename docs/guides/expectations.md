# Expectations

Expectations allow you to write your tests like you would a human-readable sentence:

```python
def test():
    data = ["hello", "world"]

    # Using the `assert` keyword
    assert isinstance(data, list)
    assert len(data) == 2
    assert "hello" in data
    assert "world" in data
    assert "goodbye" not in data

    # Using expectations
    expect(data) \
        .to.be_a_list() \
        .and_to.have_len(2) \
        .and_to.contain("hello") \
        .and_to.contain("world") \
        .and_to.have.each.be_of_type(str) \
        .and_not.contain("goodbye")
```
