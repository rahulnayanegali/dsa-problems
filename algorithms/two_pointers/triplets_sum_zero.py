
def threeSumZero(arr):
    # loop through array until last second
    # keep ith element constant
    # set two pointers i+1 and len(arr)-1th
    # check sum: if zero store in HashSet left++ and right --
    # sum < 0: left ++
    # sum > 0: right --

    result = set()
    arr.sort()

    for i in range(0, len(arr ) -2):
        left = i + 1
        right = len(arr) - 1

        while left < right:

            cur_sum = arr[i] + arr[left] + arr[right]

            if cur_sum == 0:
                result.add((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1

            elif cur_sum < 0:
                left += 1
            else:
                right -= 1

    return list(result)


print(threeSumZero([-3, 0, 1, 2, -1, 1, -2]))
