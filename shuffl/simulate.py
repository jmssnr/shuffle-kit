from .deck import Deck
from .models import Shuffle
from dataclasses import dataclass


@dataclass
class SimulationResult:
    samples: list[Deck]
    deck: Deck
    num: int


def _repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    return [shuffle(deck) for _ in range(0, num)]


def simulate(shuffle: Shuffle, deck: Deck, num: int) -> SimulationResult:
    result = _repeat(shuffle, deck, num)
    return SimulationResult(samples=result, deck=deck, num=num)
