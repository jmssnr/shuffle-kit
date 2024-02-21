import pytest
from shuffl.models import gsr, thorp, strip, cut, sequence
from shuffl import Deck
from string import ascii_lowercase
from unittest.mock import patch


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


@pytest.mark.parametrize("shuffle", [gsr, thorp, strip, cut])
def test_shuffles_mix_deck(shuffle):
    deck = Deck(range(1, 53))
    shuffled = shuffle(deck)
    assert shuffled != deck


@pytest.mark.parametrize("shuffle", [gsr, thorp, strip, cut])
def test_shuffles_work_with_string_elements(shuffle):
    deck = Deck(ascii_lowercase)
    shuffled = shuffle(deck)
    assert shuffled != deck


@pytest.mark.parametrize("shuffle", [gsr, thorp, strip, cut])
def test_shuffles_return_deck(shuffle):
    deck = Deck(range(1, 53))
    shuffled_deck = shuffle(deck)
    assert type(shuffled_deck) == Deck


@pytest.mark.parametrize("shuffle", [gsr, thorp, strip, cut])
def test_shuffle_returns_deck_with_same_number_of_elements(shuffle):
    deck = Deck(range(1, 53))
    shuffled_deck = shuffle(deck)
    assert len(deck) == len(shuffled_deck)


def test_single_gsr_shuffle_keeps_top_card_in_top_half():
    deck = Deck(range(1, 53))
    shuffled_deck = gsr(deck)
    assert shuffled_deck.index(1) < 26
