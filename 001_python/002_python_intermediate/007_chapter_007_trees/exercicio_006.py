'''
Max Heap
'''


class MaxHeap:
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
            raise IndexError("Max-Heap is empty.")
        return self.heap[0]

    def insert(self, key):
        """Inserts a new key in O(log n) time."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Swap upward while the child is GREATER than its parent
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            p = self.parent(index)
            self.heap[p], self.heap[index] = self.heap[index], self.heap[p]
            index = p

    def extract_max(self):
        """Removes and returns the maximum element in O(log n) time."""
        if not self.heap:
            raise IndexError("Max-Heap is empty.")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and restore the Max-Heap property
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)
        n = len(self.heap)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def build_heap(self, array):
        """Converts an arbitrary list into a Max-Heap in O(n) time."""
        self.heap = array[:]
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify_down(i)


# --- Example Usage ---
max_h = MaxHeap()
for val in [35, 12, 48, 7, 20, 15]:
    max_h.insert(val)

print("Internal Array:", max_h.heap)           # [48, 20, 35, 7, 12, 15]
print("Maximum (Peek):", max_h.peek())         # 48
print("Extracted Max: ", max_h.extract_max())  # 48
print("After Extract: ", max_h.heap)           # [35, 20, 15, 7, 12]
