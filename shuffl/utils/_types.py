from typing import TypeAlias, Callable
from shuffl._deck import Deck

Shuffle: TypeAlias = Callable[[Deck], Deck]
Steps: TypeAlias = list[Shuffle]
