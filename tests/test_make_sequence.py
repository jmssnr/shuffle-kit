from unittest.mock import patch

from shuffl import Deck, sequence


def test_creates_shuffle_squence_from_callables():
    with (
        patch("shuffl.gsr") as mock_riffle,
        patch("shuffl.strip") as mock_strip,
        patch("shuffl.cut") as mock_cut,
    ):
        shuffle = sequence(
            [mock_riffle, mock_riffle, mock_strip, mock_riffle, mock_cut]
        )
        shuffle(Deck([1, 2, 3]))

        assert mock_riffle.call_count == 3
        assert mock_strip.call_count == 1
        assert mock_cut.call_count == 1
