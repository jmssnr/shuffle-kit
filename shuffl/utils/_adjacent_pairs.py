from shuffl import Deck
from itertools import pairwise
from shuffl.utils._convert import _convert
from typing import Annotated
from typing_extensions import Doc


def adjacent_pairs(
    permutation: Annotated[Deck, Doc("A permutation of the original set")],
    original: Annotated[Deck, Doc("Original set")],
) -> Annotated[list[tuple], Doc("List of all adjacent pairs")]:
    """Returns all adjacent pairs in a given permutation.

    Adjacent pairs are pairs of cards that were together in the original
    deck and which are still together in the permutation.

    **Example:**

    ```python
    from shuffl.utils import adjacent_pairs
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
    permutation = _convert(permutation, original)
    return [
        (original[i], original[j]) for (i, j) in pairwise(permutation) if i + 1 == j
    ]
