from typing import Callable


def to_not_fn(fn: Callable) -> Callable:
    """Returns a function that negates the result of the provided function

    Args:
        fn (Callable): Function to negate
        *args: Arguments to pass to the function

    Returns:
        Callable: Negated function
    """

    def to_not_fn_inner(*args, **kwargs):
        res = fn(*args, **kwargs)
        assert not res[0], res[1].replace("to", "to not")

    return to_not_fn_inner