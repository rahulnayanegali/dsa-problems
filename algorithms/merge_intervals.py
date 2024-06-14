def merge(intervals):
    # Sort O(n log n)
    arr = sorted(intervals, key=lambda x: x[0])

    merged_arr = []

    for interval in arr:
        # prev[1] < next[0] -> just append
        if not merged_arr or merged_arr[-1][1] < interval[0]:
            merged_arr.append(interval)
        else:
            # if prev[1] > next[0] -> merge into one
            merged_arr[-1][1] = max(merged_arr[-1][1], interval[1])
    return merged_arr


print(merge([[1, 3], [8, 10], [2, 6], [15, 18]]))
