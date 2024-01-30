from shuffl._models import riffle
from shuffl._exceptions import DuplicateItemError, NotHashableError
from shuffl import Deck
import pytest


def test_riffle_returns_deck():
    deck = Deck([1, 2, 3])

    deck = riffle(deck)

    assert type(deck) == Deck

    with pytest.raises(DuplicateItemError):
        deck.append(1)

    with pytest.raises(NotHashableError):
        deck.append({})
