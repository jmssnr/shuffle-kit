shuffle-kit provides utilities to analyze shuffle simulations. The below code computes the empirical probabilities and cumulative distribution function.

```py
# Imports from shuffl
from shuffl import Deck, make_sequence, simulate, evaluate

# Creates a deck of 52 cards
deck = Deck(range(1, 53))

# Creates a riffle, riffle, strip, riffle, cut sequence
shuffle = make_sequence("RRSRC")

# Run 1000 simulations. After each run the deck is reset.
result = simulate(shuffle, deck, 1000)

# Evaluate the results and compute empirical probabilities and cumulative
# density function
proba, ecdf = evaluate(result)

# Get distribution, mean and standard deviation of the
# original top card
dist, mean, std = proba(1)
print(mean)
```