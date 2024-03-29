from shuffl import Deck
from shuffl.utils import adjacent_pairs
from typing import Annotated
from typing_extensions import Doc
from shuffl.models import Shuffle
import numpy as np


def adjacent(
    shuffle: Annotated[Shuffle, Doc("A shuffle model")],
    num: Annotated[int, Doc("Number of Monte-Carlo simulations")] = 1000,
) -> Annotated[
    list[list[float]], Doc("Discrete probability density function for every card")
]:
    """Returns average number of adjacent pairs.

    Adjacent pairs are pairs of cards that were together in the original
    deck and which are still together in the permutation.

    **Example:**

    ```python
    from shuffl.evaluate import adjacent
    from shuffl import Deck

    # Deck in original order
    deck = Deck(["A", "B", "C", "D", "E"])

    # Permutation of deck
    permutation = Deck(["B", "C", "A", "D", "E"])

    # Print adjacent pairs
    # [("B", "C"), ("D", "E")]
    print(adjacent(permutation, deck))
    ```
    """
    deck = Deck(range(1, 53))

    return np.mean([len(adjacent_pairs(shuffle(deck), deck)) for _ in range(num)])
