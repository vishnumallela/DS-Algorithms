#For heapify we will start process from the first index of non leaf node
#Recursion is used
#left child index is 2*index+1
#right child index is 2*index+2
#parent node (index-1)/2

def max_heapify(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[k]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)


def left(index):
    return 2*index+1


def right(index):
    return 2*index+2


def build_max_heap(A):
    # no of non-leaf levels
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(A, i)


A= [3,9,2,1,4,5]
build_max_heap(A)
print(A)

