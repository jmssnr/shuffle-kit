from shuffl import Deck, gsr, sequence, thorp
import numpy as np
import plotly.graph_objects as go


def monte_carlo(deck: Deck, shuffle) -> float:
    """Monte-Carlo simulation of New Age Solitaire.

    Args:
        deck (_type_): Initial deck
        shuffle (_type_): Shuffle to mix the initial deck

    Returns:
        float: Probability that player A wins
    """
    return np.mean([round(deck, shuffle) for _ in range(1000)])


def round(deck: Deck, shuffle) -> bool:
    """One round of New Age Solitaire.

    Args:
        deck (_type_): Initial deck
        shuffle (_type_): Shuffle to mix the initial deck

    Returns:
        bool: Player A wins
    """
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


deck = Deck(range(1, 53))
num_shuffles = range(1, 16)

result = {}

result["gsr"] = [monte_carlo(deck, sequence([gsr] * num)) for num in num_shuffles]
result["thorp"] = [monte_carlo(deck, sequence([thorp] * num)) for num in num_shuffles]

fig = go.Figure()

for k in result.keys():
    fig.add_trace(go.Scatter(x=list(num_shuffles), y=result[k], name=k))

fig.show()
