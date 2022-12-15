from __future__ import annotations

from typing import Any, Dict, Optional, Union

from .qualifier_bag import QualifierBag


class Expectation:
    """Immutable container for expecation specifications."""

    __slots__ = ("_actual", "_qualifiers")

    def __init__(
        self,
        actual: Any,
        *,
        qualifiers: Optional[Union[Dict, QualifierBag]] = None,
        **kwargs,
    ):
        self._actual = actual
        self._qualifiers = (
            QualifierBag(qualifiers) if qualifiers else QualifierBag(**kwargs)
        )

    @property
    def actual(self) -> Any:
        """Property accessor for ``_actual``."""
        return self._actual

    @property
    def qualifiers(self) -> QualifierBag:
        """Property accessor for ``_qualifiers``."""
        return self._qualifiers

    @property
    def is_strict(self) -> bool:
        """Whether or not the current evaluation will be strict."""
        return bool(self.qualifiers.strict)

    @property
    def is_negated(self) -> bool:
        """Whether or not the current evaluation will be negated."""
        return bool(self.qualifiers.negated)

    @property
    def strict(self):
        """Evaluate expectation in *strict* mode."""
        self.qualifiers.strict = True
        return self

    @property
    def strictly(self):
        """Alias for the ``strict`` property."""
        return self.strict

    @property
    def loose(self):
        """Evaluate expectation in *loose* mode, the opposite of *strict*."""
        self.qualifiers.strict = False
        return self

    @property
    def loosely(self):
        """Alias for the ``loose`` property."""
        return self.loose

    @property
    def to(self):
        """Evaluate expectation without negating subsequent assertions in the chain."""
        self.qualifiers.negated = False
        return self

    @property
    def to_not(self):
        """Evaluate expectation while negating subsequent assertions in the chain."""
        self.qualifiers.negated = True
        return self

    @property
    def and_to(self):
        """Chainable alias of ``to`` to improve the expecation readability."""
        return self.to

    @property
    def does(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def also(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def be(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def been(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def that(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def which(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def have(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def has(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def at(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def but(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def of(self):
        """Chainable property to improve the expecation readability."""
        return self

    @property
    def and_to_not(self):
        """Chainable alias of ``to_not`` to improve the expecation readability."""
        return self.to_not

    @property
    def and_not(self):
        """Chainable alias of ``to_not`` to improve the expecation readability."""
        return self.to_not

    @property
    def does_not(self):
        """Chainable alias of ``to_not`` to improve the expecation readability."""
        return self.to_not

    @property
    def but_not(self):
        """Chainable alias of ``to_not`` to improve the expecation readability."""
        return self.to_not

    def clear(self):
        """Return an immutable ``Expectation`` with all ``qualifiers`` reset."""
        return self.get_or_create(actual=self.actual)

    @classmethod
    def get_or_create(
        cls,
        actual: Any,
        *,
        qualifiers: Optional[Union[Dict, QualifierBag]] = None,
        **kwargs,
    ):
        """Factory method to create ``Expectations`` or return an existing."""
        if isinstance(actual, cls):
            return actual

        return cls(actual=actual, qualifiers=qualifiers, **kwargs)
