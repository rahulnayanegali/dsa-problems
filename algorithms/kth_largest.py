import heapq

def findKthLargest(nums, k):
    k_nums = nums[:k]
    heapq.heapify(k_nums)

    for i in range(k, len(nums)-k):
        heapq.heappop(k_nums)
        heapq.heappush(k_nums, nums[i])

    return heapq.heappop(k_nums)


print(findKthLargest([5, 7, 9, 1, 3], 2))
#9,7,5,3,1