import os



with open('IntegerArray.txt') as f:
    content = f.read().splitlines()

f.close()

intArray = [int(numeric_string) for numeric_string in content]


def bruteInversion(array):
    count = 0

    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                count += 1


    return count



def countSplitInversion(A, B):

    # divide A into 2 parts which are sorted
    # we merge and count split inversions along the way

    splitInvs = 0

    C = []

    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            splitInvs += len(A) - i


    # exhausted A
    if i == len(A):
        while j < len(B):
            C.append(B[j])
            j += 1

    # exhausted B
    elif j == len(B):
        while i < len(A):
            C.append(A[i])
            i += 1

    return C, splitInvs

def countInversion(A):

    half = len(A)//2

    inversions = 0

    if len(A) == 1:
        return A, 0

    else:

        left_arr, left_inv = countInversion(A[:half])
        right_arr, right_inv = countInversion(A[half:])
        merged_arr, split_inv = countSplitInversion(left_arr, right_arr)

    return merged_arr, left_inv + right_inv + split_inv



print(countInversion(intArray)[1])





