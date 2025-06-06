class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._items[-1]

    def clear(self):
        self._items.clear()

    def is_empty(self):
        return len(self._items) == 0

    def to_list(self):
        return list(self._items)
