from shuffl.models import Shuffle
from shuffl import Deck
from typing import Annotated
from typing_extensions import Doc


def _repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    return [shuffle(deck) for _ in range(0, num)]


def frequencies(
    shuffle: Annotated[Shuffle, Doc("A shuffle model")],
    deck: Annotated[Deck, Doc("Initial deck of cards")],
    num: Annotated[int, Doc("Number of Monte-Carlo simulations")] = 1000,
) -> Annotated[
    list[list[float]], Doc("Discrete probability density function for every card")
]:
    """Computes the discrete probability density function resulting
    from applying the given shuffle to the given initial deck of cards via
    Monte-Carlo simulations.

    **Example:**

    ```python
    from shuffl.models import gsr, sequence
    from shuffl.evaluate import frequencies
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Creates a shuffle sequence of 6 riffle shuffles
    # following the Gilbert-Shannon-Reeds model
    shuffle = sequence([gsr]*6)

    # Compute the discrete probability density function
    # for all 52 cards via a Monte-Carlo simulation with
    # 10000 iterations
    proba = frequencies(shuffle, deck, 10000)

    # Print the results for the initial top card
    print(proba[0])
    ```
    """
    samples = _repeat(shuffle, deck, num)

    return [
        [sum([i == e.index(card) for e in samples]) / num for i in range(len(deck))]
        for card in deck
    ]
