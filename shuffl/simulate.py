from .deck import Deck
from .models import Shuffle


def _repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    return [shuffle(deck) for _ in range(0, num)]


def _evaluate_probabilities(result: list[Deck], deck: Deck) -> list[list]:
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


class SimulationResult:
    def __init__(
        self, initial_deck: Deck, result: list[Deck], proba: list[list]
    ) -> None:
        self._result = result
        self._proba = proba
        self._initial_deck = initial_deck

    @property
    def initial_deck(self):
        return self._initial_deck

    @property
    def result(self):
        return self._result

    @property
    def proba(self):
        return self._proba


def simulate(shuffle: Shuffle, deck: Deck, num: int) -> SimulationResult:
    result = _repeat(shuffle, deck, num)
    proba = _evaluate_probabilities(result, deck)
    return SimulationResult(deck, result, proba)
