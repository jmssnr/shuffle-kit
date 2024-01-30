"""Provides a list implementation that only allows hashable and unique elements.
"""


from typing import Hashable, Iterable

from ._exceptions import DuplicateItemError, NotHashableError


def _check_valid_iterable(iterable: Iterable) -> "Deck":
    lst = list()
    seen = set()
    for item in iterable:
        _check_valid_item(item, seen)
        seen.add(item)
        lst.append(item)
    return lst


def _check_valid_item(item: Hashable, seen: "Deck") -> None:
    if not isinstance(item, Hashable):
        raise NotHashableError(
            f"All elements must be hashable. Element: '{item!r}' is not hashable"
        )

    if item in seen:
        raise DuplicateItemError(
            f"No duplicates allowed! Item: '{item!r}' already exists"
        )


class Deck(list):
    """A list which only allows hashable and unique elements."""

    def __init__(self, iterable: Iterable) -> None:
        deck = _check_valid_iterable(iterable)
        super().__init__(deck)

    def insert(self, index: int, item: Hashable) -> None:
        _check_valid_item(item, self)
        super().insert(index, item)

    def append(self, item: Hashable) -> None:
        _check_valid_item(item, self)
        super().append(item)
