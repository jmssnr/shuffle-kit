from shuffl import gsr
from shuffl import Deck
import numpy as np


def main():
    result = []
    for _ in range(1000):
        deck = Deck(range(1, 53))
        i = 0
        while deck.index(52) != 0:
            i = i + 1
            deck = gsr(deck)
        result.append(i)
    print(np.mean(result))


if __name__ == "__main__":
    main()
