import heapq


def findKthLargest(nums, k):
    k_nums = nums[:k]
    heapq.heapify(k_nums)

    for i in range(k, len(nums)):
        if nums[i] > k_nums[0]:
            heapq.heappop(k_nums)
            heapq.heappush(k_nums, nums[i])

    return k_nums[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# 9,7,5,3,1
