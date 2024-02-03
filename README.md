
![logo](./docs/logos/shuffl-logo-small.png)

[![Build & Publish Package Documentation](https://github.com/jmssnr/shuffle-kit/actions/workflows/docs.yaml/badge.svg)](https://github.com/jmssnr/shuffle-kit/actions/workflows/docs.yaml)

**shuffle-kit** is a Python package for modelling and analyzing playing card shuffles.

You can use it to answer questions such as:

- What is the probability of finding a certain card at a certain position after a shuffle?
- Is there a bias in a particular shuffle sequence?
- Given two shuffles, which one is more thorough?

and many more.

# Installation

## Dependencies

shuffle-kit requires:

- Python (>= 3.11)
- Numpy (>= 1.26.3)

## User installation

The easiest way to install shuffle-kit is via pip:

```pip install shuffl```

# Usage

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