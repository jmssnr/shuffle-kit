"""
This module provides different functions to evaluate shuffle models
based on Monte-Carlo simulations.

The implemented functions include:

- `adjacent`: Returns average number of adjacent pairs in a permutation
- `frequencies`: Returns empirical probabilities
- `guess`: Returns average number of correct guesses of the top card 
- `risingseq`: Returns average number of rising sequences in a permutation
- `solitaire`: Returns probability of Player A winning at the game New Age Solitaire
"""

from ._adjacent import adjacent
from ._frequencies import frequencies
from ._guessing import guess
from ._solitaire import solitaire

__all__ = [adjacent, frequencies, guess, solitaire]
