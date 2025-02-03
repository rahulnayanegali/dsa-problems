import heapq


class Task:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x[0])

    max_cpu_load = 0
    current_cpu_load = 0
    min_heap = []

    for job in jobs:
        start, end, cpu_load = job
        while min_heap and min_heap[0].end <= start:
            ended_job = heapq.heappop(min_heap)
            current_cpu_load -= ended_job.cpu_load
        print(Task(start, end, cpu_load))

        heapq.heappush(min_heap, Task(start, end, cpu_load))
        current_cpu_load += cpu_load

        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load


test_cases = [
    ([[1,4,3], [2,5,4], [7,9,6]], 7),
    ([[1,4,2], [2,4,1], [3,6,5]], 8),
    ([[1,3,5], [4,6,3], [7,9,2]], 5),
    ([[1,4,2], [1,5,3], [1,6,4]], 9),
    ([[1,5,2], [2,5,3], [3,5,4]], 9),
    ([[1,5,5]], 5),
    ([], 0),
    ([[1,10,3], [2,8,2], [3,6,1], [5,9,4], [7,11,2]], 12),
    ([[1,3,0], [2,4,0], [3,5,1]], 1),
    ([[1,5,5], [100,105,10], [200,210,15]], 15)
]

for i, (jobs, expected) in enumerate(test_cases, 1):
    result = find_max_cpu_load(jobs)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    print(f"  Input: {jobs}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}\n")