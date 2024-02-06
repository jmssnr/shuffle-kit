In order to analyze a particular shuffle, we typically want to simulate the shuffle several times and each time record the outcome. The below code snippet uses the `simulate` utility function to simulate the given shuffle sequence 100 times.

```py
from shuffl import Deck, make_sequence, simulate

deck = Deck(["A", "B", "C", "D"])

shuffle = make_sequence("RSRC")

result = simulate(shuffle, deck, 100)
```