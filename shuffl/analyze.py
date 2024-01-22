from typing import Hashable, Tuple, Callable
from itertools import accumulate
from math import sqrt, log
from .simulate import SimulationResult


def _confidence_bands(result: SimulationResult, alpha: float) -> float:
    num = len(result.result)
    return sqrt(log(2 / alpha) / 2 / num)


def empirical_cdf(
    result: SimulationResult, alpha: float = 0.95
) -> Callable[[Hashable], Tuple[list[float], float]]:
    eps = _confidence_bands(result, alpha)

    def ecdf(card: Hashable) -> Tuple[list[float], float]:
        idx = result.initial_deck.index(card)
        return (list(accumulate(result.proba[idx])), eps)

    return ecdf
