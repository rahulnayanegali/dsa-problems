import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Add the new ele to max_heap
        heapq.heappush(self.max_heap, -num)

        # Balance both heaps by sending largest ele of max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # heapify to keep len(max_heap) >= len(min_heap)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:

        # return largest ele of max_heap of odd
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


medianFinder = MedianFinder()
medianFinder.addNum(1)  # arr = [1]
medianFinder.addNum(2)  # arr = [1, 2]
medianFinder.findMedian()  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # arr[1, 2, 3]
medianFinder.findMedian()  # return 2.0
