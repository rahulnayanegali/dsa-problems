def is_interval_conflicts(intervals):
    # sort intervals based on their start time
    print(intervals)

    sorted_itervals = sorted(intervals, key=lambda x: x[0])
    print(sorted_itervals)

    conflicts = []

    for i in range(len(sorted_itervals)):
        for j in range(i + 1, len(sorted_itervals)):
            if sorted_itervals[i][1] > sorted_itervals[j][0]:
                conflicts.append((sorted_itervals[i], sorted_itervals[j]))
            else:
                break

    return conflicts


conflicts2 = is_interval_conflicts([[1, 5], [3, 7], [2, 6], [10, 15], [5, 6], [4, 100]])
conflicts1 = is_interval_conflicts([[4,5], [2,3], [3,6], [5,7], [7,8]])
for conflict in conflicts1:
    print(f"{conflict[0]} and {conflict[1]} conflict.")
