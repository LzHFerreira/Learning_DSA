from queue import Queue
from collections import deque

# Queue implementation using collections.deque, of course thats FIFO


class MyQueue:
    def __init__(self):
        # Initialize an empty deque to store queue elements
        self.queue = deque()

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    
#bellow code makew it a deque
    def rear(self):
        # Return the item at the rear of the queue without removing it
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self.queue[-1]