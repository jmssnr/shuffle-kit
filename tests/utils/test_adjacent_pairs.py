from shuffl.utils import adjacent_pairs
from shuffl import Deck


def test_adjacent_for_strings():
    deck = Deck(["A", "B", "C", "D", "E"])
    permutation = Deck(["B", "C", "A", "D", "E"])
    pairs = adjacent_pairs(permutation, deck)
    assert pairs == [("B", "C"), ("D", "E")]


def test_adjacent_for_integers():
    deck = Deck(range(1, 53))
    pairs = adjacent_pairs(deck, deck)
    assert len(pairs) == 51
