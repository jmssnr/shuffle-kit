from typing import Hashable, Tuple, Callable
from itertools import accumulate
from math import sqrt, log
from ._simulate import SimulationResult

EmpiricalCDF = Callable[[Hashable], Tuple[list[float], float]]
EmpiricalProbability = Callable[[Hashable], Tuple[list[float], float, float]]


def _confidence_bands(result: SimulationResult, alpha: float) -> float:
    return sqrt(log(2 / alpha) / 2 / result.num)


def _empirical_probability(result: SimulationResult) -> EmpiricalProbability:
    def proba(card: Hashable) -> Tuple[list[float], float, float]:
        lst = []
        for i in range(0, len(result.deck)):
            sublist = []
            for e in result.samples:
                sublist.append(i == e.index(card))
            lst.append(sum(sublist) / result.num)

        mean = sum([p * idx for idx, p in enumerate(lst, 1)])
        std = sqrt(sum([(idx - mean) ** 2 * p for idx, p in enumerate(lst, 1)]))
        return lst, mean, std

    return proba


def _empirical_cdf(
    proba: EmpiricalProbability, result: SimulationResult, alpha: float = 0.95
) -> EmpiricalCDF:
    eps = _confidence_bands(result, alpha)

    def ecdf(card: Hashable) -> Tuple[list[float], float]:
        return (list(accumulate(proba(card))), eps)

    return ecdf


def evaluate(
    result: SimulationResult, alpha: float = 0.95
) -> Tuple[EmpiricalProbability, EmpiricalCDF]:
    proba = _empirical_probability(result)

    ecdf = _empirical_cdf(proba, result, alpha)

    return proba, ecdf
