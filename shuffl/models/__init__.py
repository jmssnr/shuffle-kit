"""
This module provides several different mathematical models for shuffling cards.

The implemented models include:

- `gsr`: Gilbert-Shannon-Reeds model for riffle shuffling
- `thorp`: Thorp model for riffle shuffling
- `strip`: Coin-toss model for strip or overhand shuffling
- `cut`: Model for cutting a deck about in half
"""

from ._cut import cut
from ._gsr import gsr
from ._strip import strip
from ._thorp import thorp
from ._sequence import sequence, Shuffle

__all__ = [cut, gsr, strip, thorp, sequence, Shuffle]
