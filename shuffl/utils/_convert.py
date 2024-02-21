from shuffl import Deck


def convert(permutation: Deck, original: Deck) -> list[int]:
    return [original.index(c) for c in permutation]
