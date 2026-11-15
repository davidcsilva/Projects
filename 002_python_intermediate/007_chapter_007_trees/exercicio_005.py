'''
Min-Heap
'''


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def insert(self, key):
        """Inserts a new key in O(log n) time."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            p = self.parent(index)
            self.heap[p], self.heap[index] = self.heap[index], self.heap[p]
            index = p

    def extract_min(self):
        """Removes and returns the minimum element in O(log n) time."""
        if not self.heap:
            raise IndexError("Heap is empty.")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and restore the heap property
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def build_heap(self, array):
        """Transforms an arbitrary list into a valid heap in O(n) time."""
        self.heap = array[:]
        # Start from the last non-leaf node and heapify down
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify_down(i)


# --- Example Usage ---
h = MinHeap()
for val in [35, 12, 48, 7, 20, 15]:
    h.insert(val)

print("Internal Array:", h.heap)           # [7, 12, 15, 35, 20, 48]
print("Minimum (Peek):", h.peek())         # 7
print("Extracted Min: ", h.extract_min())  # 7
print("After Extract: ", h.heap)           # [12, 20, 15, 35, 48]
