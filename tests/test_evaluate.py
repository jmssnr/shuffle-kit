from shuffl._simulate import SimulationResult
from shuffl import Deck, evaluate


def test_empirical_probability():
    deck = Deck(["A", "B", "C"])

    samples = [["A", "C", "B"], ["B", "A", "C"], ["A", "C", "B"]]

    result = SimulationResult(samples=samples, deck=deck, num=3)

    proba, _ = evaluate(result)

    dist, _, _ = proba("A")

    assert dist == [2 / 3, 1 / 3, 0]


def test_empirical_cdf():
    deck = Deck(["A", "B", "C"])

    samples = [["A", "C", "B"], ["B", "A", "C"], ["A", "C", "B"]]

    result = SimulationResult(samples=samples, deck=deck, num=3)

    _, ecdf = evaluate(result)

    f, _ = ecdf("A")

    assert f == [2 / 3, 1, 1]
