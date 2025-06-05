# Data structure with a heads that points to the 2nd node, that points to 3rd and so on,
# until the tail. As a result, is of eassy storage in comparison with an array, f.e. but
# has O(n) for insert, read and delete


# The node, aka the basic
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Implementing a double linked list
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # Link the new node to the current head
        # Check if the list is empty
        if self.head:
            self.head.prev = new_node
        # If the list is empty, set tail to new node
        else:
            self.tail = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)  # Create a new node with the given value
        new_node.prev = self.tail  # Link the new node to the current tail
        # Check if the list is empty
        if self.tail:
            self.tail.next = new_node
        # If the list is empty, set head to new node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_front(self, value):
        if not self.head:  # Check if the list is empty
            return None

        removed_value = self.head.value  # Store the value to be removed
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:  # Check if the list is empty
            return None

        removed_value = self.tail.value  # Store the value to be removed
        self.tail = self.tail.prev  # Update the tail to the previous node

        if self.tail:
            self.tail.next = None  # Disconnect the removed node
        else:
            self.head = None  # If the list becomes empty, update the head

        return removed_value

    def find_from_head(self, value):
        current = self.head  # Start from the head of the list
        while current:  # Traverse the list until the end
            if current.value == value:  # Check if the current node's value matches
                return current  # Return the node if found
            current = current.next  # Move to the next node
        return None  # Return None if the value is not found

    def find_from_tail(self, value):
        current = self.tail  # Start from the tail of the list
        while current:  # Traverse the list until the beginning
            if current.value == value:  # Check if the current node's value matches
                return current  # Return the node if found
            current = current.prev  # Move to the previous node
        return None  # Return None if the value is not found

    def remove_by_value(self, value):
        if not self.head:  # Check if the list is empty
            return None
        
        current = self.head

        while current:  # Traverse the list
            if current.value == value:  # Found the node to remove
                if current.prev:  
                    current.prev.next = current.next  # Link previous to next
                else:  
                    self.head = current.next  # If it's the head, update head
                
                if current.next:  
                    current.next.prev = current.prev  # Link next to previous
                else:  
                    self.tail = current.prev  # If it's the tail, update tail

                return current.value  # Return removed value
            
            current = current.next  # Move to the next node
        
        return None  # Value not found