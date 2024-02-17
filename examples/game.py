from shuffl.games import guessing_game
from shuffl import gsr, Deck, sequence

# Creates a list of integers from 1..52, representing a
# standard deck of 52 cards
deck = Deck(range(1, 53))

# Creates a sequence of two riffle shuffles following
# the Gilbert-Shannon-Reeds model
shuffle = sequence([gsr, gsr])

# Run a simulation of the guessing game described in
# Bayer D., Diaconis P. (1992). Trailing the dovetail shuffle to its lair.
# The Annals of Applied Probability, Vol. 2, No. 2, 294-313
correct_guess = guessing_game(deck, shuffle)

# Print the number of correct guesses. On average this should
# be around 19.
print(f"Number of correct guesses: {correct_guess}")
