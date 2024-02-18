from shuffl import Deck, sequence, thorp, risingseq, Shuffle
import numpy as np

# Creates a list of integers from 1..52, representing a
# standard deck of 52 cards
deck = Deck(range(1, 53))

# Set-up iterable for number of shuffles
num_shuffles = range(1, 16)


# Helper for Monte-Carlo simulation
def monte_carlo(deck: Deck, shuffle: Shuffle) -> float:
    return np.mean([risingseq(shuffle(deck))[1] for _ in range(1000)])


# Compute average number of rising sequences for an increasing number
# of shuffles following the Thorp model for riffle shuffling
for num in num_shuffles:
    shuffle = sequence([thorp] * num)
    num_seq = monte_carlo(deck, shuffle)
    print(f"No. Shuffles: {num}, Avg. No. Rising Sequences: {num_seq}")
