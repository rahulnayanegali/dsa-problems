def merge(left, right):
    print(left, right)
    result = []
    left_index = 0
    right_index = 0

    # Compare elements from left and right arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Concatenate remaining elements of left array (if any)
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Concatenate remaining elements of right array (if any)
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort(array):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    middle_index = len(array) // 2
    left_array = array[:middle_index]
    right_array = array[middle_index:]

    # Recursively sort both halves and merge them
    return merge(merge_sort(left_array), merge_sort(right_array))


# Example usage
unsorted_array = [34, 7, 23, 32, 5, 62]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)  # Output: [5, 7, 23, 32, 34, 62]
