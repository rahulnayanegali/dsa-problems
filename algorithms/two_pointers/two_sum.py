# If the input array is sorted

def two_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        ans = arr[left] + arr[right]

        if ans == target:
            return [left, right]

        if ans > target:
            right -= 1
        else:
            left += 1
    return -1


print(two_sum([2,7,11,15], 9)) # [0,1]
print(two_sum([-10, -3, 4, 5, 6], 1)) # [1,2]
print(two_sum([1, 2, 3, 4, 5, 1000000], 1000005)) # [4,5]
print(two_sum([1,2,3,4,5,6,7,8,9,10], 19)) # [8,9]
print(two_sum([1,2], 3)) # [0,1]
print(two_sum([-3, -1, 0, 1, 2, 4], 0)) # [1,3]



