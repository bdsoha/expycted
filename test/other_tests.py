from expycted import expect
import pytest


@pytest.mark.parametrize("v1,true", [
    (1, False),
    (3, False),
    (3.2, False),
    ('a', True),
    ([1, 2], True),
    (set(), True),
    (tuple(), True),
    ('123', True),
    (lambda x: x, False),
]
)
def test_has_len(v1, true):
    assert expect(v1).to._has_len() == true
