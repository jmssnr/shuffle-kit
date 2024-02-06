In this tutorial we are going to look at how you can use shuffle-kit to create playing card shuffle models.

The easiest and fastest way to create a model with shuffle-kit is to use the `make_sequence` function. The below code creates a model for the _riffle, strip, riffle, cut_
shuffle sequence.

```py
from shuffl import Deck, make_sequence

deck = Deck(["A", "B", "C", "D"])

shuffle = make_sequence("RSRC")

shuffled_deck = shuffle(deck)

print(f"Initial deck: {deck}")
print(f"Shuffled deck: {shuffled_deck}")
```

