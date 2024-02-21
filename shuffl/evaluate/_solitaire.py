from shuffl import Deck
from shuffl.models import Shuffle
import numpy as np
from typing import Annotated, Doc


def _round(deck: Deck, shuffle: Shuffle) -> bool:
    n = int(len(deck) / 2)
    top, bottom = deck[:n], deck[: n - 1 : -1]
    shuffled_deck = shuffle(deck)
    while (len(top) > 0) and (len(bottom) > 0):
        card = shuffled_deck.pop(0)
        if card == top[0]:
            top.pop(0)
        elif card == bottom[0]:
            bottom.pop(0)
        else:
            shuffled_deck.append(card)
    return len(top) == 0


def solitaire(
    shuffle: Annotated[Shuffle, Doc("A shuffle model")],
    deck: Annotated[Deck, Doc("Initial deck of cards")],
    num: Annotated[int, Doc("Number of Monte-Carlo simulations")] = 1000,
) -> Annotated[float, Doc("Probability of player A winning")]:
    """Probability of Player A winning at the game New Age Solitaire
    determined via Monte-Carlo simulations.

    **Example:**

    ```python
    from shuffl.evaluate import solitaire
    from shuffl import Deck
    from shuffl.models import sequence, gsr

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Create a shuffle model
    shuffle = sequence([gsr]*10)

    # Evaluate the probability of player A
    # winning. For a well-mixed deck the expected
    # probability is 0.5
    print(solitaire(shuffle, deck, 100000))
    ```
    """
    return np.mean([_round(deck, shuffle) for _ in range(num)])
