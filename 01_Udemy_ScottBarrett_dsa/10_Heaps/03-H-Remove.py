# remove() --> we only remove the top/root, doesn't matter if its minHeap or maxHeap.


class MaxHeap:
    def __init__(self):
        self.heap = []  # a list called heap

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # 1. Is there a left child and is it bigger than current?
            if (left_index < len(self.heap)) and (
                self.heap[left_index] > self.heap[max_index]
            ):
                max_index = left_index

            # 2. Is there a right child and is it bigger than the BIGGEST so far?
            if (right_index < len(self.heap)) and (
                self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index

            # 3. If the largest value is not the parent, SWAP
            if max_index != index:
                self._swap(index, max_index)
                index = max_index  # Move down to the new index and repeat
            else:
                return  # The parent is already bigger than both children!

    def remove(self):
        # case1: heap is empty.
        if len(self.heap) == 0:
            return None

        # case2: there is only 1 item in the heap (or list)
        if len(self.heap) == 1:
            return self.heap.pop()

        # case3: 2 or more items in heap
        max_value = self.heap[0]
        # move the last item to the root
        self.heap[0] = self.heap.pop()
        # call a helper method to sink it down
        self._sink_down(0)

        return max_value


myheap = MaxHeap()

myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()
print(myheap.heap)


myheap.remove()
print(myheap.heap)
