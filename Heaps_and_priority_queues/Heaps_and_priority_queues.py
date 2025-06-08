import heapq  # Python's built-in heapq module implements a min-heap


class MinHeap:
    def __init__(self):
        self.heap = []  # Internal list to store heap elements

    def push(self, item):
        """
        Add a new item to the heap.
        Time complexity: O(log n)
        """
        heapq.heappush(self.heap, item)

    def pop(self):
        """
        Remove and return the smallest item from the heap.
        Time complexity: O(log n)
        """
        if not self.heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self.heap)

    def peek(self):
        """
        Return the smallest item without removing it.
        Time complexity: O(1)
        """
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def heapify(self, iterable):
        """
        Build a heap from an iterable of items.
        Time complexity: O(n)
        """
        self.heap = list(iterable)
        heapq.heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


# Example usage:
if __name__ == "__main__":
    # Create a min-heap and insert elements
    h = MinHeap()
    for value in [5, 3, 8, 1, 2]:
        h.push(value)
        print(f"Inserted {value}: {h}")

    # Peek at the smallest element
    print(f"Peek: {h.peek()}")

    # Remove elements in priority order (smallest first)
    while len(h):
        print(f"Popped: {h.pop()} Heap now: {h}")

    # Heapify an existing list
    data = [10, 4, 7, 3, 9]
    h.heapify(data)
    print(f"Heapified list: {h}")

    # Priority queue example: (priority, task)
    pq = MinHeap()
    pq.push((2, "low priority"))
    pq.push((1, "high priority"))
    pq.push((3, "lowest priority"))
    print("\nPriority queue order:")
    while len(pq):
        print(pq.pop())
