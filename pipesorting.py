#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    # NOTICE: The sorted list must be returned.
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        sort_list(lefthalf)
        sort_list(righthalf)
        
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1
    return A

    L = 0
    R = len(A)-1
    while L <= R:
        m = floor((L+R)/2)
        if A[m] < T:
            L = m+1
        elif A[m] > T:
            R = m-1
        else:
            return m


def find(A, lower, upper):
    # NOTICE: The result must be returned.

    L = 0
    R = len(A)-1
    start = lower
    end = upper
    while L <= R:
        m = (L+R)//2
        if A[m] < lower:
            if A[m] > start:
                start = A[m]
                L = m+1 # right
            else:
                break
        else:
            R = m-1

    L = 0
    R = len(A)-1

    while L <= R:
        m = (L+R)//2
        if A[m] < upper:
            L = m+1
        else:
            if A[m] > end:
                R = m-1
            else:
                break


    return start, end


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
