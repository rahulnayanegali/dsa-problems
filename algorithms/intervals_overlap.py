
# https://www.geeksforgeeks.org/check-interval-completely-overlaps/
def is_interval_overlap(intervals):
    # sort intervals based on their start time
    print(intervals)

    sorted_itervals = sorted(intervals,  key= lambda x: x[0])
    print(sorted_itervals)

    for i in range(0, len(sorted_itervals)-1):
        if sorted_itervals[i][1] > sorted_itervals[i+1][0]:
            return True

    return False


print(is_interval_overlap([[1,3], [1,7], [4,8], [2,5]]))
print(is_interval_overlap([[1,3], [7,9], [4,6], [10,13]]))