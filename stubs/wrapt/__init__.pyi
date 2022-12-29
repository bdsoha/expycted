from typing import Any, Generic, TypeVar


T = TypeVar("T", bound=Any)


class ObjectProxy(Generic[T]): 
    __wrapped__ : T

    def __init__(self, wrapped: T):
        ...
