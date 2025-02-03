import heapq


class Task:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def meeting_rooms_II(intervals):
    min_heap = []
    max_rooms = 1
    intervals.sort(key=lambda x: x[0])

    for interval in intervals:
        start, end = interval
        while min_heap and start >= min_heap[0].end:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, Task(start, end))

        max_rooms = max(max_rooms, len(min_heap))

    return max_rooms


print(meeting_rooms_II([[1, 4], [2, 5], [7, 9]]))
print(meeting_rooms_II([[1,4], [2,4], [3,4], [5,6]]))
print(meeting_rooms_II([[23,2], [1,3], [2,4]]))
