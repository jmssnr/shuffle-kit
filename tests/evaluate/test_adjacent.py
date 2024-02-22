from shuffl.evaluate import adjacent
from shuffl.models import thorp, sequence


def test_average_adjacent_pairs_for_perfectly_mixed_deck():
    shuffle = sequence([thorp] * 20)
    pairs = adjacent(shuffle)
    assert (pairs < 2) and (pairs > 0)
