from .node import Node

class SortedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self._insert_into_empty(new_node)
        elif value < self.head.value:
            self._insert_at_head(new_node)
        elif value > self.tail.value:
            self._insert_at_tail(new_node)
        else:
            self._insert_in_middle(new_node)

    def _insert_into_empty(self, node):
        self.head = self.tail = node

    def _insert_at_head(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def _insert_at_tail(self, node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def _insert_in_middle(self, node):
        current = self.head
        while current and current.value < node.value:
            current = current.next
        prev = current.prev
        prev.next = node
        node.prev = prev
        node.next = current
        current.prev = node

    def to_list(self):
        return [node.value for node in self._iterate()]

    def _iterate(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def display(self):
        if not self.head:
            print("The list is empty.")
        else:
            print(" -> ".join(str(v) for v in self.to_list()))
