"""
643. Maximum Average Subarray I
    You are given an integer array nums consisting of n elements, and an integer k.
    Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

"""


def findMaxAverage(nums, k):
    if k == 1:
        return max(nums)
    # Sliding window of k size
    cur_sum = sum(nums[:k])
    max_sum = cur_sum

    # subtracting i th ele from the cur_sum and adding k+1 th ele to the sum
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, cur_sum)
    return max_sum / k
