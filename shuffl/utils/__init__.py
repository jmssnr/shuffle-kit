"""
This module provides different utility functions that facilitate
working with and analyzing shuffle models.

The implemented functions include:

- `adjacent_pairs`: Returns number of adjacent pairs in a permutation 
- `sequences`: Returns all rising and descending sequences in a permutation
"""

from ._adjacent_pairs import adjacent_pairs

__all__ = [adjacent_pairs]
