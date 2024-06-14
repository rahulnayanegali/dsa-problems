def findMaxSum(nums, k):
    # Sliding window of k size
    cur_sum = sum(nums[:k])
    max_sum = cur_sum
    print(nums[:k], cur_sum)

    # subtracting i th ele from the cur_sum and adding k+1 th ele to the sum
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, cur_sum)
        print(nums[i - k + 1:i + 1], cur_sum)
    return max_sum


print(findMaxSum([12, 1, 5, 1, 3, 2], 3))  # [12,1,5] 18
