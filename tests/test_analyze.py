from shuffl import risingseq, descendingseq, Deck, gsr, sequence, adjacent
import pytest


@pytest.mark.parametrize("n,k,expected", [(52, 3, 53), (13, 8, 14), (27, 4, 28)])
def test_sum_of_rising_descending(n, k, expected):
    deck = Deck(range(1, n + 1))
    shuffle = sequence([gsr] * k)

    shuffled = shuffle(deck)
    num_rising = risingseq(shuffled)[1]
    num_descen = descendingseq(shuffled)[1]

    assert num_rising + num_descen == expected


def test_adjacent_for_ordered_deck():
    deck = Deck(range(1, 53))
    assert adjacent(deck) == 51


def test_adjacent_for_shuffled_deck():
    deck = Deck([1, 2, 6, 10])
    assert adjacent(deck) == 1
