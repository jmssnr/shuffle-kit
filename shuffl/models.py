"""Provides several different shuffling models.

This module allows the user to model arbitrary shuffling sequences.

The module contains the following functions:

- `riffle(deck)` - Returns a shuffled list of hashable and unique elements.
- `strip(deck)` - Returns a shuffled list of hashable and unique elements.
- `cut(deck)` - Returns a shuffled list of hashable and unique elements.
"""

from typing import Callable

import numpy as np

from .deck import Deck

Shuffle = Callable[[Deck], Deck]
Steps = list[Shuffle]


def riffle(deck: Deck) -> Deck:
    """Performs a standard riffle shuffle.

    Examples:
        >>> riffle(Deck([1,2,3]))
        [2, 1, 3]

    Args:
        deck: List of hashable and unique items.

    Returns:
        Shuffled list of hashable and unique items.
    """
    x = np.sort(np.random.uniform(low=0, high=1, size=len(deck)))
    y = 2 * x % 1
    return Deck([deck[i] for i in np.argsort(y)])


def strip(deck: Deck) -> Deck:
    """Performs a strip cut.

    Args:
        deck: List of hashable and unique elements.

    Returns:
        Shuffled list of hashable and unique items.
    """
    print("strip...")
    n = len(deck)
    shuffled_deck = []
    while len(deck) > 0:
        slice = np.random.binomial(n, 0.25)
        shuffled_deck = deck[:slice] + shuffled_deck
        deck = deck[slice:]
    return Deck(shuffled_deck)


def cut(deck: Deck) -> Deck:
    """Performs a regular cut.

    Args:
        deck: List of hashable and unique elements.

    Returns:
        Shuffled list of hashable and unique items.
    """
    slice = np.random.binomial(len(deck), 0.5)
    return Deck(deck[slice:] + deck[:slice])


shuffles = {"R": riffle, "S": strip, "C": cut}


def make_sequence(steps: Steps | str) -> Shuffle:
    if type(steps) == str:
        keys_valid = [key in shuffles.keys() for key in list(steps)]

        if not all(keys_valid):
            raise KeyError("Unknown keys passed")
        try:
            steps = [shuffles[key.capitalize()] for key in list(steps)]
        except:
            raise KeyError("Unknown shuffle key - valid keys are 'R', 'S' and 'C'")

    else:
        shuffles_valid = [s in shuffles.values() for s in steps]

        if not all(shuffles_valid):
            raise KeyError("Unknown shuffle passed")

    def shuffle(deck: Deck) -> Deck:
        for step in steps:
            deck = step(deck)
        return deck

    return shuffle