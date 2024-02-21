from shuffl.evaluate import adjacent
from shuffl import Deck


def test_adjacent_for_strings():
    deck = Deck(["A", "B", "C", "D", "E"])
    permutation = Deck(["B", "C", "A", "D", "E"])
    pairs = adjacent(permutation, deck)
    assert pairs == [("B", "C"), ("D", "E")]


def test_adjacent_for_integers():
    deck = Deck(range(1, 53))
    pairs = adjacent(deck, deck)
    assert len(pairs) == 51
