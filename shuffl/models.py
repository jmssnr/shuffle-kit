import numpy as np
from typing import Callable

from ._deck import Deck

Shuffle = Callable[[Deck], Deck]
Steps = list[Shuffle]


def gsr(deck: Deck) -> Deck:
    """Gilbert-Shannon-Reeds model for riffle shuffling.

    A deck of n cards is cut about in half according to a binomial
    distribution. The cards from the two packets are then riffled in
    such a way, that the probability of dropping a card from either
    half is proportional to the respective packet size.

    There are several analogous interpretations of the GSR model.
    This function implements the geometric interpretation.

    **References**:

    - Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
    The Annals of Applied Probability, Vol. 2, No. 2, 294-313

    Args:
        deck (Deck): Initial deck

    Returns:
        Deck: The deck after riffle shuffling.
    """
    x = np.sort(np.random.uniform(low=0, high=1, size=len(deck)))
    y = 2 * x % 1
    return Deck([deck[i] for i in np.argsort(y)])


def thorp(deck: Deck) -> Deck:
    """Thorp model for riffle shuffling.

    The model cuts a deck of 2n cards into two packets of size n, and
    then starts dropping the cards from the left or right hand, such that
    each time one chooses the left or right card with probability 1/2 and
    then drops the card from the opposite hand.

    **References**:

    - Thorp E. O. (1973). Nonrandom shuffling with applications to the game of Faro.
    Journal of the American Statistical Association, Vol. 68, No. 344, 842-847.

    Args:
        deck (Deck): Initial deck

    Returns:
        Deck: The deck after riffle shuffling
    """
    n = int(len(deck) / 2)
    cointoss = np.random.binomial(1, 0.5, n)
    left, right = deck[:n], deck[n:]
    shuffled = []
    for c in cointoss:
        if c == 0:
            shuffled.extend([left.pop(0), right.pop(0)])
        else:
            shuffled.extend([right.pop(0), left.pop(0)])
    return shuffled


def strip(deck: Deck) -> Deck:
    """Coin toss model for strip cutting a deck of cards.

    The implementation is based on the coin toss interpretation
    of the strip shuffle.

    Args:
        deck (Deck): Initial deck

    Returns:
        Deck: The deck after strip cutting.
    """
    n = int(len(deck))
    cointoss = np.random.binomial(1, 0.2, n - 1)
    breakpoints = (np.flatnonzero(cointoss) + 1).tolist()
    split_packets = np.split(deck, breakpoints)
    return [s for p in reversed(split_packets) for s in p]


def cut(deck: Deck) -> Deck:
    """Model for cutting a deck about in half and completing
    the cut.

    Cuts a given deck according to a binomial distribution.

    **References:**

    - Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
    The Annals of Applied Probability, Vol. 2, No. 2, 294-313.

    Args:
        deck (Deck): Initial deck

    Returns:
        Deck: Deck of cards after cutting
    """
    cut_point = np.random.binomial(len(deck), 0.5)
    return Deck(deck[cut_point:] + deck[:cut_point])


def sequence(steps: list[Shuffle]) -> Shuffle:
    """Chains individual shuffles into a sequence of shuffles.

    Args:
        steps (list[Shuffle]): Individual shuffle models

    Returns:
        Shuffle: Sequence composed of individual shuffle models
    """

    def shuffle(deck: Deck) -> Deck:
        for step in steps:
            deck = step(deck)
        return deck

    return shuffle
