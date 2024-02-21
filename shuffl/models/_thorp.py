import numpy as np
from shuffl import Deck
from typing import Annotated
from typing_extensions import Doc


def thorp(
    deck: Annotated[Deck, Doc("A deck of cards")],
) -> Annotated[Deck, Doc("The shuffled deck")]:
    """Thorp model for riffle shuffling.

    The model cuts a deck of _2n_ cards into two packets of size n, and
    then starts dropping the cards from the left or right hand, such that
    each time one chooses the left or right card with probability 1/2 and
    then drops the card from the opposite hand.

    **Example:**

    ```python
    from shuffl.models import thorp
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Apply the shuffle
    shuffled_deck = thorp(deck)

    # Print the shuffled deck
    print(shuffled_deck)
    ```

    **References:**

    - Thorp E. O. (1973). Nonrandom shuffling with applications to the game of Faro.
    Journal of the American Statistical Association, Vol. 68, No. 344, 842-847.
    """
    n = int(len(deck) / 2)
    cointoss = np.random.binomial(1, 0.5, n)
    left, right = deck[:n], deck[n:]
    shuffled = []
    for c in cointoss:
        if c == 0:
            shuffled.extend([left.pop(0), right.pop(0)])
        else:
            shuffled.extend([right.pop(0), left.pop(0)])
    return Deck(shuffled)
