from shuffl.models import strip
from shuffl.exceptions import DuplicateItemError, NotHashableError
from shuffl import Deck
import pytest


def test_strip_returns_deck():
    deck = Deck([1, 2, 3])

    deck = strip(deck)

    assert type(deck) == Deck

    with pytest.raises(DuplicateItemError):
        deck.append(1)

    with pytest.raises(NotHashableError):
        deck.append({})
