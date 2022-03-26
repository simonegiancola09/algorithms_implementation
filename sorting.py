from msilib.schema import Binary
from priority_queues import BinaryHeap
def merge(array, lo, mid, hi):
    '''
    merge for merge-sort algorithm
    assumes the two lists are sorted
    merges in place
    '''
    lower_len = mid - lo + 1
    upper_len = hi - mid
    lower = [None] * lower_len
    upper = [None] * upper_len
    for i in range(lower_len):
        lower[i] = array[i]
    for i in range(upper_len):
        upper[i] = array[mid + i]
    
    i = 0 # index of lower
    j = 0 # index of upper
    k = 0 # index of array
    while i < lower_len and j < upper_len:
        if lower[i] < upper[j]:
            array[k] = lower[i]
            i += 1
        else:
            array[k] = upper[j]
            j += 1
        k += 1
    # either one of the two is exhausted
    while i < lower_len:
        array[k] = lower[i]
        i += 1
        k += 1
    while j < upper_len:
        array[k] = upper[j]
        j += 1
        k += 1

def merge_sort(array, lo, hi):
    mid = (hi + lo - 1) // 2
    merge_sort(array, lo, mid)
    merge_sort(array, mid + 1, hi)
    merge(array, lo, mid, hi)

def counting_sort(l, maxElem):
    '''
    Highly inefficient for big arrays
    '''
    big_list = [0] * maxElem
    for x in l:
        big_list[x] += 1
    for i in range(maxElem):
        for j in range(big_list[i]):
            print(big_list[i])
    
    
def heap_sort(l):
    '''
    Very good, exploits binary heap structure, computational time is 2Nlog(N)
    '''
    out = []
    heap = BinaryHeap()
    for x in l:
        heap.insert(x)
    while len(heap) != 0:
        el = heap.remove_max()
        el.append(out)
    return out
    