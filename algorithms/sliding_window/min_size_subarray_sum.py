def minSubArrayLen(target, nums):
    n = len(nums)
    min_sum_arr = float('inf')
    cur_sum = 0
    start = 0
    for end in range(len(nums)):
        cur_sum += nums[end]

        while cur_sum >= target:
            min_sum_arr = min(min_sum_arr, end - start + 1)
            cur_sum -= nums[start]
            start += 1

    return 0 if min_sum_arr == float('inf') else min_sum_arr
