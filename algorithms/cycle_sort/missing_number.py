"""
https://leetcode.com/problems/missing-number/description/?submissionId=894460002
"""


def xor_swap(arr, i, j):
    if i != j:
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def missingNumber(arr):
    i = 0
    n = len(arr)
    while i < n:
        # [1,5,2,3,4]
        cur_ele = arr[i]
        if cur_ele < n and arr[i] != arr[cur_ele]:
            xor_swap(arr, i, cur_ele)
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return len(arr)
