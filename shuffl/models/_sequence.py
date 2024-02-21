from shuffl import Deck
from typing import Annotated, TypeAlias, Callable
from typing_extensions import Doc

Shuffle: TypeAlias = Callable[[Deck], Deck]


def sequence(
    steps: Annotated[list[Shuffle], Doc("List of shuffle models")],
) -> Annotated[Shuffle, Doc("Sequence of composed shuffle models")]:
    """Chains individual shuffles into a sequence of shuffles.

    **Example:**

    ```python
    from shuffl.models import gsr, strip, cut sequence
    from shuffl import Deck

    # Create a deck of 52 cards
    deck = Deck(range(1,53))

    # Define riffle, riffle, strip, riffle, cut sequence
    shuffle = sequence([gsr, gsr, strip, gsr, cut])

    # Apply the shuffle
    shuffled_deck = shuffle(deck)

    # Print the shuffled deck
    print(shuffled_deck)
    ```
    """

    def shuffle(deck: Deck) -> Deck:
        for step in steps:
            deck = step(deck)
        return deck

    return shuffle
