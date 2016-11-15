#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    root = Node()
    for t in ordliste:
        word, pos = list(t)
        last = root
        for l in word:
            n = last.barn.get(l)
            if n is None:
                n = last.barn[l] = Node()
            last = n

        last.posi.append(pos)
    return root


def posisjoner(ord, indeks, node):
    if indeks == len(ord):
        return node.posi
    l = ord[indeks]
    pos = []
    if l == "?":
        for a in "abcdefghijklmnopqrstuvwxyz":
            b = node.barn.get(a)
            if b is not None:
                pos += posisjoner(ord, indeks+1, b)
    else:
        b = node.barn.get(l)
        if b is not None:
            pos += posisjoner(ord, indeks+1, b)
    return pos
   

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()

