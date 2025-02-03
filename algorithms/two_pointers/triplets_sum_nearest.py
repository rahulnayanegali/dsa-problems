def threeSumNearest(arr, target):
    triplet_sum = float('inf')
    arr.sort()

    for i in range(0, len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]

            if abs(target - cur_sum) < abs(target - triplet_sum):
                triplet_sum = cur_sum

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return cur_sum

    return triplet_sum


# Test cases
print(threeSumNearest([-1, 2, 1, -4], 1))  # Expected output: 2
print(threeSumNearest([0, 0, 0], 1))  # Expected output: 0
