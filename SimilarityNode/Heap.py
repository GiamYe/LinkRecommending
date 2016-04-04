__author__ = 'zhenan'

from Node import Node

def min_heapify(arr, i):
    l = 2*i
    r = 2*i+1
    least = i
    if l < len(arr):
        if arr[l] < arr[i]:
            least = l
        else:
            least = i
    if r < len(arr):
        if arr[r] < arr[least]:
            least = r
    if least != i:
        arr[i], arr[least] = arr[least], arr[i]
        min_heapify(arr, least)

def build(arr):
    count = len(arr)/2
    while (count > 0):
        min_heapify(arr, count)
        count = count - 1
    return arr


def get_min(arr):
    if len(arr)<2:
        return 'underflow'
    min = arr[1]
    size = len(arr)
    arr[1] = arr[size-1]
    del(arr[size-1])
    min_heapify(arr, 1)
    return min

def insert(arr=[], key=None):
    arr.append(key)
    i = len(arr)-1
    parent = i/2
    while i>1 and arr[parent]>arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent
        parent = i/2
    return arr



if __name__ == '__main__':
    arr = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    A = []
    for i in arr:
        A.append(Node('v', i))
    Arr = build(A)
    print build(arr)
    print Arr

    print insert(Arr, Node('v',5))

    print get_min(Arr)
    print Arr


