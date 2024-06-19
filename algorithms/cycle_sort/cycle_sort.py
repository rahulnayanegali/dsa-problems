'''
The input array has to be in the range (1-n)
'''


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def xor_swap(arr, i, j):
    if i != j:
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]


def cycle_sort(arr):
    """
    Syntax
    :param arr:
    :return: sorted array

    Pseudocode
    [3,5,2,1,4]
    Start from first item and keep swapping the i's to their respective position until arr[0] = 1
    Increment i and do the same thing.
    """
    i = 0
    while i < len(arr):
        # [1,5,2,3,4]
        if arr[i] != i + 1:
            xor_swap(arr, i, arr[i] - 1)
        else:
            i += 1
    return arr


print(cycle_sort([3, 5, 2, 1, 4]))
