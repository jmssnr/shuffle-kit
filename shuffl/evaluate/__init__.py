"""
This module provides different functions to evaluate shuffle models.

The implemented functions include:

- `adjacent`: Return all adjacent pairs in a permutation
- `frequencies`: Computes empirical probabilities from Monte-Carlo simulations
- `guess`: Evaluates shuffles based on the ability to guess cards 
- `risings`: Return all rising sequences in a permutation
- `descendants`: Return all descendants in a permutation
- `solitaire`: Evaluates results for playing New Age Solitaire
"""

from ._adjacent import adjacent
from ._frequencies import frequencies
from ._guessing import guess
from ._sequences import risings, descendants
from ._solitaire import solitaire

__all__ = [adjacent, frequencies, guess, risings, descendants, solitaire]
