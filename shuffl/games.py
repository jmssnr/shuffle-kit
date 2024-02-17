from ._deck import Deck
from ._models import Shuffle
from itertools import groupby
from operator import itemgetter


def _strategy(draw: int, seen_cards, initial_deck):
    if draw == 0:
        return initial_deck[0]

    longest_block_of_possible_cards = max(
        [list(p) for i, p in groupby(enumerate(seen_cards), itemgetter(1)) if i == 0],
        key=len,
    )

    top_card_index = longest_block_of_possible_cards[0][0]

    guess = initial_deck[top_card_index]

    return guess


def guessing_game(initial_deck: Deck, shuffle: Shuffle) -> int:
    """A guesser has to guess the top card of a face down
    shuffled deck of cards. After each guess the top card is revealed
    and then discared.

    The expected number of guesses is about 4.5 for a well-shuffled deck.
    The guessing game can thus be used to compare different shuffles.

    **References:**

    - Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
    The Annals of Applied Probability, Vol. 2, No. 2, 294-313.

    Args:
        initial_deck (Deck): The initial deck
        shuffle (Shuffle): Shuffle model

    Returns:
        int: Number of correct guesses.
    """
    num_cards = len(initial_deck)
    wins = []
    seen_cards = [0] * num_cards

    shuffled_deck = shuffle(initial_deck)

    for draw in range(num_cards):
        guess = _strategy(draw, seen_cards, initial_deck)
        top_card = shuffled_deck.pop(0)
        seen_cards[initial_deck.index(top_card)] = 1
        wins.append(top_card == guess)
    return sum(wins)