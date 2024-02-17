![logo](./docs/logos/shuffle-kit-logo-small.png)

[![docs](https://github.com/jmssnr/shuffle-kit/actions/workflows/docs.yaml/badge.svg)](https://github.com/jmssnr/shuffle-kit/actions/workflows/docs.yaml)_![PyPI - Version](https://img.shields.io/pypi/v/shuffl)_[![Test](https://github.com/jmssnr/shuffle-kit/actions/workflows/test.yaml/badge.svg)](https://github.com/jmssnr/shuffle-kit/actions/workflows/test.yaml)

**shuffle-kit** is a Python package for modelling and analyzing playing card shuffles.

It implements several mathematical models of commonly used shuffles that can be composed into complex sequences.

In addition, several utility functions are provided to faciliate analyzing the various shuffle models.

# Installation

## Dependencies

shuffle-kit requires:

- Python (>= 3.11)
- Numpy (>= 1.26.3)

## User installation

The easiest way to install shuffle-kit is via pip:

`pip install shuffle-kit`

# Examples

## Basic example of using shuffle-kit

```py
from shuffl import gsr, strip, cut, sequence, simulate, Deck
from itertools import accumulate

# Creates a list of integers from 1..52, representing a
# standard deck of 52 cards
deck = Deck(range(1,53))

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
```

## Simulating a guessing game

Here we play a round of the guessing game described in Bayer and Diaconis (1992). Consider a shuffled deck of 52 cards, face down on the table. The task is to guess the top card. After each guess, the top card is turned over and discarded. 

If the deck is perfectly shuffled the average number of correct guesses is around 4.5. However, if the deck is riffle shuffled _k_ times, then there exists a conjectural optimal strategy that achives a higher number of correct guesses depending on _k_.

```py
from shuffl.games import guessing_game
from shuffl import gsr, Deck, sequence

# Creates a list of integers from 1..52, representing a
# standard deck of 52 cards
deck = Deck(range(1, 53))

# Creates a sequence of two riffle shuffles following
# the Gilbert-Shannon-Reeds model
shuffle = sequence([gsr, gsr])

# Run a simulation of the guessing game described in
# Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
# The Annals of Applied Probability, Vol. 2, No. 2, 294-313
correct_guess = guessing_game(deck, shuffle)

# Print the number of correct guesses. On average this should
# be around 19.
print(f"Number of correct guesses: {correct_guess}")
```
