# Approach
"""
Using Two pointers:
    1. First set two pointers.
    2. Initiate an empty array to return squares.
    3. Compare two pointers ignoring sign
    4. store the largest square value in the array
"""


def sort_array_squares(arr):
    left = 0
    right = len(arr) - 1
    res = [None] * len(arr)
    arr_index = len(arr) - 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            res[arr_index] = arr[left] ** 2
            left += 1
            arr_index -= 1
        else:
            res[arr_index] = arr[right] ** 2
            right -= 1
            arr_index -= 1
    return res


print(sort_array_squares([-2, -1, 0, 1, 4]))
print(sort_array_squares([-4, -1, 0, 3, 10]))
print(sort_array_squares([-7, -3, 2, 3, 11]))
