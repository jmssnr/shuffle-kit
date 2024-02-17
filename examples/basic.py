from shuffl import gsr, strip, cut, sequence, simulate, Deck
from itertools import accumulate

# Creates a list of integers from 1..52, representing a
# standard deck of 52 cards
deck = Deck(range(1, 53))

# Creates a riffle, riffle, strip, riffle, cut shuffle sequence
# with the Gilbert-Shannon-Reeds model for riffle shuffling
shuffle = sequence([gsr, gsr, strip, gsr, cut])

# Simulate the shuffle a 1000 times. For each simulation, the
# deck is reset to the initial order
result = simulate(shuffle, deck, 1000)

# Compute the empirical cumulative density function of the
# original top card, i.e., "1"
ecdf = list(accumulate(result.probability[0]))

# Print the probability that the original top card ("1") is
# found within the top ten cards after shuffling
print(f"Probability of finding '1' within the top ten cards: {ecdf[9]:.2}")
