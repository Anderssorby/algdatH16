#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict, deque


alphabet = "abcdefghijklmnopqrstuvwxyz"


def findf(A, j):
    def find(i):
        if len(A[i]) > j:
            return alphabet.find(A[i][j])
        else:
            return 0
    return find

def quicksort(A):
    print("A =", A)
    if len(A) <= 1:
        return A
    i = 0
    # q = len(A)//2
    q = randint(0, len(A)-1)
    left = deque()
    right = deque()
    pivot = A[q]
    print("pivot =", A[q])
    while i < len(A): 
        if A[i] <= pivot:
            left.append(A[i])
        else:
            right.append(A[i])

        i += 1
    print("left =", left)
    print("right =", right)
    if not right:
        return left
    else:
        left = quicksort(left)
        right = quicksort(right)
        return  left + right


def subsort(A, j):
    print("A =", A)
    if len(A) <= 1:
        return A
    f = findf(A, j)
    i = 0
    q = len(A)//2
    left = deque()
    right = deque()
    pivot = f(q)
    print("pivot =", A[q])
    while i < len(A): 
        if len(A[i]) <= j:
            left.append(A[i])
            i += 1
            continue
        l = f(i)
        if l <= pivot:
            left.append(A[i])
        else:
            right.append(A[i])

        i += 1
    print("left =", left)
    print("right =", right)
    if not right:
        return left
    else:
        left = subsort(left, j)
        right = subsort(right, j)
 
def digits(n):
    while n > 10:
        yield n % 10
        n //= 10
    yield n


def radixsort(A, d):
    j = 0
    while j < d:
        B = [0]*10
        i = 0
        while i < len(A):
            B[A[i]] += 1
            i += 1
        print(B)
        C = [0]*len(A)
        i = 1
        while i < len(B):
            B[i] += B[i-1]
            i += 1
        print(B)
        i = len(A)-1
        while i >= 0:
            C[B[A[i]]-1] = A[i]
            B[A[i]] -= 1
            i -= 1
        return C
        


def countsort(A, d):
    # f = findf(A, j)
    B = [0]*d
    i = 0
    while i < len(A):
        B[A[i]] += 1
        i += 1
    print(B)
    C = [0]*len(A)
    i = 1
    while i < len(B):
        B[i] += B[i-1]
        i += 1
    print(B)
    i = len(A)-1
    while i >= 0:
        C[B[A[i]]-1] = A[i]
        B[A[i]] -= 1
        i -= 1
    return C


def stablesort(A, j):
    a = findf(A, j)
    B = [0]*len(alphabet)
    i = 0
    while i < len(A):
        B[a(i)] += 1
        i += 1
    C = [0]*len(A)
    i = 1
    while i < len(B):
        B[i] += B[i-1]
        i += 1
    i = len(A)-1
    while i >= 0:
        C[B[a(i)]-1] = A[i]
        B[a(i)] -= 1
        i -= 1
    return C


def flexradix(A, d):
    j = d
    sort = deque()
    while j >= 0:
        A = stablesort(A, j)
        # print("A sorted at ", j, A)
        j -= 1        

    return A
        


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
