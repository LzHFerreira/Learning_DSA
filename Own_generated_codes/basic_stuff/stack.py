class Stack:
    #
    # A simple stack implementation using a Python list.
    # Follows Last-In-First-Out (LIFO) principle.
    #

    def __init__(self):
        # Initialize an empty stack.
        self.items = []

    def is_empty(self):
        # Check if the stack is empty.
        # Returns True if stack is empty, False otherwise.
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack.
        # item: The item to be added.
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack.
        # Returns the item at the top of the stack.
        # Raises IndexError if the stack is empty.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top item of the stack without removing it.
        # Returns the item at the top of the stack.
        # Raises IndexError if the stack is empty.
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack.
        # Returns the size of the stack.
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top item:", stack.peek())  # Output: 3
    print("Stack size:", stack.size())  # Output: 3
    print("Popped:", stack.pop())  # Output: 3
    print("Is empty?", stack.is_empty())  # Output: False
