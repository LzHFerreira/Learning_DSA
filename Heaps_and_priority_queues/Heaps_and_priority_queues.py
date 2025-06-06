# Heaps and Priority Queues in Python
# -----------------------------------
# A heap is a specialized tree-based data structure that satisfies the heap property:
#   - In a max-heap, for any given node, the value is greater than or equal to its children.
#   - In a min-heap, for any given node, the value is less than or equal to its children.
# Heaps are commonly implemented as binary heaps using arrays for efficiency.
#
# A priority queue is an abstract data type where each element has a "priority."
# Elements are served based on priority (highest or lowest), not just insertion order.
# Heaps are the most efficient way to implement priority queues.
#
# Time Complexity:
#   - Insertion: O(log n)
#   - Extract-min/extract-max: O(log n)
#   - Peek (get min/max): O(1)
#   - Heapify (build heap from list): O(n)
# Space Complexity: O(n)
#
# Reasoning:
#   - Heaps allow fast access to the highest (max-heap) or lowest (min-heap) priority element.
#   - The binary heap is a complete binary tree, so it can be efficiently stored in an array.
#   - The parent/child relationship is easily calculated with indices:
#       - Parent: (i-1)//2
#       - Left child: 2*i+1
#       - Right child: 2*i+2
#   - Used in algorithms like Dijkstra's, Prim's, and for scheduling tasks.
#
# Example Usage Cases:
#   - Task scheduling (OS, CPU job queues)
#   - Graph algorithms (Dijkstra's shortest path, Prim's MST)
#   - Real-time event simulation
#   - Bandwidth management, load balancing
#   - Implementing data structures like median heaps

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
