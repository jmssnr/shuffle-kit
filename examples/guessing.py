from shuffl import gsr, sequence
from shuffl.games import guessing_game
from shuffl import Deck
import numpy as np


def main():
    initial_deck = Deck(range(1, 53))
    num_sim = 100000

    for num_shuffles in range(1, 11):
        shuffle = sequence([gsr] * num_shuffles)
        avg = np.mean([guessing_game(initial_deck, shuffle) for _ in range(num_sim)])
        print(f"k = {num_shuffles}, Average Wins: {avg}")


if __name__ == "__main__":
    main()
