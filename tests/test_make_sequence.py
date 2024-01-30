from unittest.mock import Mock, patch

from shuffl import Deck
from shuffl._models import make_sequence, shuffles


def test_creates_shuffle_sequence_from_string_input():
    with patch.dict(
        shuffles, {"R": Mock(), "S": Mock(), "C": Mock()}, clear=True
    ) as mock_shuffles:
        shuffle = make_sequence("RRSRC")
        shuffle(Deck([1, 2, 3]))
        assert mock_shuffles["R"].call_count == 3
        assert mock_shuffles["S"].call_count == 1
        assert mock_shuffles["C"].call_count == 1


def test_creates_shuffle_squence_from_callables():
    with (
        patch("shuffl.riffle") as mock_riffle,
        patch("shuffl.strip") as mock_strip,
        patch("shuffl.cut") as mock_cut,
        patch.dict(
            shuffles, {"R": mock_riffle, "S": mock_strip, "C": mock_cut}, clear=True
        ),
    ):
        shuffle = make_sequence(
            [mock_riffle, mock_riffle, mock_strip, mock_riffle, mock_cut]
        )
        shuffle(Deck([1, 2, 3]))

        assert mock_riffle.call_count == 3
        assert mock_strip.call_count == 1
        assert mock_cut.call_count == 1
