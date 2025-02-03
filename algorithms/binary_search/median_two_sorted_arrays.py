import math


def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)
    half = math.ceil(total / 2)

    l = (0 + len(nums1) - 1) // 2

    r = half - l - 2
    print(nums1[l])
    print(nums2[r])

    # while True:
    #     if nums1[l] <= nums2[r + 1] and nums1[r] <= nums1[l + 1]:
    #
    #         break
    #
    #     if nums1[r] > nums1[l + 1]:
    #         r -= 1
    #         l += 1
    #     elif nums1[l] > nums2[r + 1]:
    #         l -= 1
    #         r += 1
    #
    # if total % 2:
    #     return (max(nums1[l], nums2[r]) + min(nums1[l + 1], nums2[r + 1])) / 2
    #
    # else:
    #     return max(nums1[l], nums2[r])


findMedianSortedArrays([1, 3], [2])
