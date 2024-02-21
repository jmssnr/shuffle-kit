from shuffl import Deck
import numpy as np
from typing import Annotated, Doc


def gsr(
    deck: Annotated[Deck, Doc("A deck of cards")],
) -> Annotated[Deck, Doc("The shuffled deck")]:
    """Gilbert-Shannon-Reeds model for riffle shuffling.

    A deck of n cards is cut about in half according to a binomial
    distribution. The cards from the two packets are then riffled in
    such a way, that the probability of dropping a card from either
    half is proportional to the respective packet size.

    There are several analogous interpretations of the GSR model.
    This function implements the geometric interpretation.

    **Example:**

    ```python
    from shuffl.models import gsr
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Apply the shuffle
    shuffled_deck = gsr(deck)

    # Print the shuffled deck
    print(shuffled_deck)
    ```

    **References:**

    - Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
    The Annals of Applied Probability, Vol. 2, No. 2, 294-313
    """
    x = np.sort(np.random.uniform(low=0, high=1, size=len(deck)))
    y = 2 * x % 1
    return Deck([deck[i] for i in np.argsort(y)])
