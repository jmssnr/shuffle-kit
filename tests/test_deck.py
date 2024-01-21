import pytest

from shuffl import Deck
from shuffl.exceptions import DuplicateItemError, NotHashableError


def test_does_not_allow_duplicate_on_init():
    with pytest.raises(DuplicateItemError):
        Deck([1, 1])


def test_does_not_allow_duplicate_on_append():
    deck = Deck([1, 2])
    with pytest.raises(DuplicateItemError):
        deck.append(2)


def test_does_not_allow_duplicate_on_insert():
    deck = Deck([1, 2])
    with pytest.raises(DuplicateItemError):
        deck.insert(1, 1)


def test_does_not_allow_unhashable_item_on_init():
    with pytest.raises(NotHashableError):
        Deck([1, 2, {}])


def test_does_not_allow_unhashable_item_on_append():
    deck = Deck([1, 2])
    with pytest.raises(NotHashableError):
        deck.append({})


def test_does_not_allow_unhashable_item_on_insert():
    deck = Deck([1, 2])
    with pytest.raises(NotHashableError):
        deck.insert(1, {})
