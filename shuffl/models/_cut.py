from shuffl import Deck
import numpy as np
from typing import Annotated
from typing_extensions import Doc


def cut(
    deck: Annotated[Deck, Doc("A deck of cards")],
) -> Annotated[Deck, Doc("The shuffled deck")]:
    """Model for cutting a deck about in half and completing
    the cut.

    Cuts a given deck according to a binomial distribution.

    **Example:**

    ```python
    from shuffl.models import cut
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Apply the shuffle
    shuffled_deck = cut(deck)

    # Print the shuffled deck
    print(shuffled_deck)
    ```

    **References:**

    - Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
    The Annals of Applied Probability, Vol. 2, No. 2, 294-313.
    """
    cut_point = np.random.binomial(len(deck), 0.5)
    return Deck(deck[cut_point:] + deck[:cut_point])
