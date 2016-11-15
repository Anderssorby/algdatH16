#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    string = ""
    while len(decks) != 0:
        ldeck = decks[0]
        least = ldeck[0]
        li = 0
        for deck in decks:
            if deck[0][0] < least[0]:
                least = deck[0]
                ldeck = deck
        ldeck.remove(least)
        string += least[1]
        if len(ldeck)==0:
            decks.remove(ldeck)

    return string

        
            
    


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
