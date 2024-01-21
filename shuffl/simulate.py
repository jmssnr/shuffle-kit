from .deck import Deck
from .models import Shuffle
from typing import Hashable
from enum import StrEnum, auto
from itertools import accumulate
from math import sqrt, log


class SearchTypes(StrEnum):
    ITEM = auto()
    POSITION = auto()


class SimulationResult:
    @staticmethod
    def evaluate(deck: Deck, result: list[Deck]) -> list[list]:
        matrix = []
        num = len(result)
        for card in deck:
            lst = []
            for i in range(0, len(deck)):
                sublist = []
                for e in result:
                    sublist.append(i == e.index(card))
                lst.append(sum(sublist) / num)
            matrix.append(lst)
        return matrix

    def __init__(self, samples: list[Deck], initial_deck: Deck) -> None:
        self._samples = samples
        self._initial_deck = initial_deck
        self.proba = self.evaluate(initial_deck, samples)

    @property
    def initial_deck(self) -> Deck:
        return self._initial_deck

    @property
    def samples(self) -> list[Deck]:
        return self._samples

    def _get_position(self, search: Hashable, type: SearchTypes) -> int:
        if type == SearchTypes.POSITION:
            return search
        elif type == SearchTypes.ITEM:
            return self.initial_deck.index(search)

    def _get_confidence_bands(self, alpha: float):
        num = len(self.samples)
        return sqrt(log(2 / alpha) / 2 / num)

    def empirical_cdf(
        self, search: Hashable, type: SearchTypes = "position", alpha: float = 0.95
    ):
        pos = self._get_position(search, type)
        eps = self._get_confidence_bands(alpha)
        return (list(accumulate(self.proba[pos])), eps)


def _repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    return [shuffle(deck) for _ in range(0, num)]


def simulate(shuffle: Shuffle, deck: Deck, num: int) -> SimulationResult:
    result = _repeat(shuffle, deck, int)
    return SimulationResult(sample=result, initial_deck=deck)
