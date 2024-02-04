# Create and use your first model

```py
from shuffl import make_sequence, Deck

deck = Deck(["A", "B", "C", "D", "E", "F"])

# Alternatively you can pass models directly in a list, e.g.,
# shuffle = make_sequence([riffle, strip, riffle, cut])
shuffle = make_sequence("RSRC") 
 
shuffled_deck = shuffle(deck)

print(f"Before shuffle: {deck}")
print(f"After shuffle: {shuffled_deck}")

```
