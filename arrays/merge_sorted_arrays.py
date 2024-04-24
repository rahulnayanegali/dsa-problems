
def merge_sorted_arrays(arr1, arr2):
    left = 0
    right = 0
    merged_arr = []

    while left < len(arr1) and right < len(arr2):
        if arr1[left] < arr2[right]:
            merged_arr.append(arr1[left])
            left += 1
        else:
            merged_arr.append(arr2[right])
            right += 1

    # if either of elements are left out
    merged_arr.extend(arr1[left:])

    merged_arr.extend(arr2[right:])

    return merged_arr

print(merge_sorted_arrays([1, 2, 3, 3, 4], [4, 5, 6]))
