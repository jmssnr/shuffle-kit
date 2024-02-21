from shuffl import Deck
import numpy as np
from typing import Annotated
from typing_extensions import Doc


def strip(
    deck: Annotated[Deck, Doc("A deck of cards")],
) -> Annotated[Deck, Doc("The shuffled deck")]:
    """Coin toss model for strip cutting a deck of cards.

    The implementation is based on the coin toss interpretation
    of the strip shuffle.

    **Example:**

    ```python
    from shuffl.models import strip
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Apply the shuffle
    shuffled_deck = strip(deck)

    # Print the shuffled deck
    print(shuffled_deck)
    ```
    """
    n = int(len(deck))
    cointoss = np.random.binomial(1, 0.2, n - 1)
    breakpoints = (np.flatnonzero(cointoss) + 1).tolist()
    split_packets = np.split(deck, breakpoints)
    return Deck([s for p in reversed(split_packets) for s in p])
