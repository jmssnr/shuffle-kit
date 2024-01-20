from .deck import Deck
from .models import Shuffle


def repeat(shuffle: Shuffle, deck: Deck, num: int) -> list[Deck]:
    """Repeats a shuffle n times.

    Given an initial deck, the provided shuffle is repeated
    'num' of times. After each shuffle the deck is reset to
    its initial state.

    Args:
        shuffle: Shuffle. Can be a single shuffle or a sequence.
        deck: Initial deck. Each shuffle starts with this deck.
        num: Number of repetitions of the provided shuffle.

    Returns:
        The shuffled deck for each repetition.
    """
    return [shuffle(deck) for _ in range(0, num)]
