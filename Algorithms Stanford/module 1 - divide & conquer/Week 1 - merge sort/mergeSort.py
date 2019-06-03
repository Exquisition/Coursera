

def merge(A, B):

    C = []

    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

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

    return C


def mergeSort(A):

    n = len(A)//2

    if len(A) <= 1:
        return A

    else:
        return merge(mergeSort(A[:n]), mergeSort(A[n:]))


print(mergeSort([3,5,24,9,4,1,2]))







