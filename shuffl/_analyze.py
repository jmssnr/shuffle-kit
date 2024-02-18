from ._deck import Deck
from ._models import Shuffle
from dataclasses import dataclass
from typing import Tuple


@dataclass
class SimulationResult:
    samples: list[Deck]
    deck: list
    num: int
    probability: list[list[float]]


def _repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    return [shuffle(deck) for _ in range(0, num)]


def _probabilities(samples: list[Deck], deck: Deck, num: int) -> list[list[float]]:
    return [
        [sum([i == e.index(card) for e in samples]) / num for i in range(len(deck))]
        for card in deck
    ]


def simulate(shuffle: Shuffle, deck: Deck, num: int) -> SimulationResult:
    """Simulates and analyzes empirical probabilities for a given shuffle model.
    Each simulation run resets to the given initial deck.

    Args:
        shuffle (Shuffle): Shuffle model
        deck (Deck): Initial deck
        num (int): Number of simulations

    Returns:
        SimulationResult: Result object
    """
    result = _repeat(shuffle, deck, num)
    proba = _probabilities(result, deck, num)
    return SimulationResult(samples=result, probability=proba, deck=deck, num=num)


def _empirical_cdf():
    raise NotImplementedError


def _mean():
    raise NotImplementedError


def _std():
    raise NotImplementedError


def risingseq(deck: list[int]) -> Tuple[list[list], int]:
    """Iteratively determines all rising sequences in a
    given list of integers.

    Args:
        deck (list[int]): List of unique integers

    Returns:
        Tuple[list[list], int]: List of all rising sequences and total
        number of rising sequences
    """
    deck = deck.copy()
    sequences = []
    while len(deck) > 0:
        card = deck.pop(0)
        subseq = [card]
        for i in range(len(deck)):
            if subseq[-1] + 1 == deck[i]:
                subseq.append(deck[i])
        sequences.append(subseq)
        for i in subseq[1:]:
            deck.pop(deck.index(i))
    return sequences, len(sequences)
