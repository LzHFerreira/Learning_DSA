class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class SortedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)  # Create a new node with the given value

        # If the list is empty, set both head and tail to the new node
        if not self.head:
            self.head = self.tail = new_node
            return

        # If the new value is less than the head's value, insert at the beginning
        if value < self.head.value:
            new_node.next = self.head      # Link new node to current head
            self.head.prev = new_node      # Link current head back to new node
            self.head = new_node           # Update head to new node
            return

        # If the new value is greater than the tail's value, insert at the end
        if value > self.tail.value:
            new_node.prev = self.tail      # Link new node back to current tail
            self.tail.next = new_node      # Link current tail to new node
            self.tail = new_node           # Update tail to new node
            return

        # Otherwise, find the correct position in the middle
        current = self.head
        # Traverse the list to find where to insert the new value
        while current and current.value < value:
            current = current.next

        # Insert new_node before 'current'
        prev_node = current.prev
        prev_node.next = new_node      # Link previous node to new node
        new_node.prev = prev_node      # Link new node back to previous node
        new_node.next = current        # Link new node to current node
        current.prev = new_node        # Link current node back to new node
    # The show_list method is defined below with the correct implementation.

    def user_choice(self):
        while True:
            choice = input("Enter a number to add to the sorted list, 'q' to quit, or 's' to show the list: ")
            if choice.lower() == 'q':
                print("Exiting the program.")
                break
            elif choice.lower() == 's':
                self.show_list()
            else:
                try:
                    value = int(choice)
                    self.add(value)
                    print(f"Added {value} to the sorted list.")
                except ValueError:
                    print("Please enter a valid integer or 'q' to quit.")

    def show_list(self):
        # Start from the head of the list
        current = self.head
        # If the list is empty, print a message and return
        if not current:
            print("The list is empty.")
            return
        values = []  # This will store the values of each node as strings
        # Traverse the list from head to tail
        while current:
            values.append(str(current.value))  # Add the current node's value to the list
            current = current.next  # Move to the next node
        # Join all values with ' -> ' and print the result
        print(" -> ".join(values))


if __name__ == "__main__":
    sl = SortedList()
    sl.user_choice()
