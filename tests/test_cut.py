from shuffl._models import cut
from shuffl._exceptions import DuplicateItemError, NotHashableError
from shuffl import Deck
import pytest


def test_cut_returns_deck():
    deck = Deck([1, 2, 3])

    deck = cut(deck)

    assert type(deck) == Deck

    with pytest.raises(DuplicateItemError):
        deck.append(1)

    with pytest.raises(NotHashableError):
        deck.append({})


def test_cut_burries_top_card():
    deck = Deck(range(1, 53))

    deck = cut(deck)

    assert deck.index(1) > 1
