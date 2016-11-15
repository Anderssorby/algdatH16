#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin


def get(self, i):
    try:
        return self[i]
    except IndexError:
        return None


def parent(A, i):
    return A.get(i//2)


def left(A, i):
    return A.get(2*i)

def right(A, i):
    return A.get(2*i+1)


def max_heapify(A, i):
    l = left(A, i)
    r = right(A, i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest is not i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest)


def build_max_heap(A):
    A.heap_size = len(A)
    i = len(A)//2
    while i >= 1:
        max_heapify(A, i)
        i -= 1


def heapsort(A):
    build_max_heap(A)
    i = 0
    while i < A.heap_size:
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        A.heap_size -= 1
        max_heapify(A, largest)
        


def binary_graph(A):
    # SKRIV DIN KODE HER
    # Du må mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for å løse oppgaven
    # Funksjonen skal returnere koordinatene til hver node i en heap
    A.get = get 
    pos = []

    i = 0
    # find the leftmost node
    leftmost = None
    while left(A, i) is not '-':
        leftmost = left(A, i)
        i += 1

    x = 0
    y = 0
    i = 0
    node = leftmost
    while i < len(A):
        node = A[i]





def main():
    A = stdin.readline().strip().split(" ")
    print(binary_graph(A), end='')


if __name__ == "__main__":
    main()
