class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        if self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            self.heapify_up(self.get_parent_index(index))

    def remove_min(self):
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return value

    def heapify_down(self, index):
        smallest = index
        if self.has_left_child(index) and self.heap[smallest] > self.left_child(index):
            smallest = self.get_left_child_index(index)
        if self.has_right_child(index) and self.heap[smallest] > self.right_child(index):
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def display_heap(self):
        return self.heap


heap = MinHeap()
heap.insert(5)
heap.insert(20)
heap.insert(10)
heap.insert(8)

print(heap.display_heap())
heap.remove_min()
print(heap.display_heap())