
import os
import statistics

with open('data.txt') as f:
    content = f.read().splitlines()

f.close()

intArray = [int(numeric_string) for numeric_string in content]


comparisons = 0

def swap(ar, i, j):
    ar[i], ar[j] = ar[j], ar[i]


def firstPivot(A, l, r):
    return l, A[l]

def lastpivot(A, l, r):
    return r, A[r]

def medianpivot(A, l, r):
    midIndex = (l+r)//2

    mid = A[midIndex]

    left = A[l]
    right = A[r]

    arr = [mid, left, right]
    median = statistics.median(arr)

    indMedian = A.index(median)

    return indMedian, median


def partition(A, l, r, method):

    pivotIndex, p = method(A, l, r)

    if method == lastpivot or method == medianpivot:
        swap(A, l, pivotIndex)


    i = l+1

    for j in range(l+1, r+1):
        if A[j] < p:
            # swap A[i] and A[j]
            A[i], A[j] = A[j], A[i]
            i += 1


    A[l], A[i-1] = A[i-1], A[l]

    return i-1





def quicksort(A, l, r):

    global comparisons

    if l < r:

        pivot = partition(A, l, r, medianpivot)

        comparisons += r - l

        quicksort(A, l, pivot-1)


        quicksort(A, pivot+1, r)


    return A


a = quicksort(intArray, 0, len(intArray)-1)

print(comparisons)