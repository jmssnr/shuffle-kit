from shuffl import Deck


def _convert(permutation: Deck, original: Deck) -> list[int]:
    return [original.index(c) for c in permutation]
