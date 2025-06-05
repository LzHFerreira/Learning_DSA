# First, we create a stack to hold the actions.
# Then we define a way to log actions and undo them.
# Finally, we demonstrate the undo functionality.


class PerformActions:
    def __init__(self):
        self.items = []  # Stack for performed actions
        self.undone = []  # Stack for undone actions (for redo)

    def client_action(self, action):
        print(f"Performing action: {action}")  # Print the action being performed
        self.push(action)  # Add the action to the performed stack
        self.undone.clear()  # Clear the redo stack on new action

    def is_empty(self):
        return len(self.items) == 0  # Return True if no performed actions

    def push(self, item):
        self.items.append(item)  # Add an item to the performed actions stack

    def pop(self):
        if self.is_empty():  # Check if there are actions to pop
            raise IndexError("pop from empty stack")  # Raise error if stack is empty
        return self.items.pop()  # Remove and return the last performed action

    def peek(self):
        if self.is_empty():  # Check if stack is empty
            raise IndexError("peek from empty stack")  # Raise error if stack is empty
        return self.items[-1]  # Return the last performed action without removing it

    def size(self):
        return len(self.items)  # Return the number of performed actions

    def undo(self):
        if self.is_empty():  # Check if there are actions to undo
            print("Nothing to undo.")  # Inform user if nothing to undo
            return
        action = self.pop()  # Remove the last performed action
        self.undone.append(action)  # Add it to the undone stack for redo
        print(f"Undid action: {action}")  # Inform user of the undone action

    def redo(self):
        if not self.undone:  # Check if there are actions to redo
            print("Nothing to redo.")  # Inform user if nothing to redo
            return
        action = self.undone.pop()  # Remove the last undone action
        self.push(action)  # Add it back to the performed actions stack
        print(f"Redid action: {action}")  # Inform user of the redone action

    def show_actions(self):
        print(
            "Current actions stack:", self.items
        )  # Show the stack of performed actions
        print("Undone actions stack:", self.undone)  # Show the stack of undone actions


if __name__ == "__main__":
    pa = PerformActions()  # Create an instance of PerformActions
    while True:  # Start a loop for CLI interaction
        cmd = (
            input(
                "Enter action, 'undo', 'redo', 'show', or 'q' to quit: "
            )  # Prompt user for input
            .strip()  # Remove leading/trailing whitespace
            .lower()  # Convert input to lowercase
        )
        if cmd == "q":  # If user enters 'q', exit the loop
            print("Exiting.")  # Inform user of exit
            break
        elif cmd == "undo":  # If user enters 'undo'
            pa.undo()  # Call undo method
        elif cmd == "redo":  # If user enters 'redo'
            pa.redo()  # Call redo method
        elif cmd == "show":  # If user enters 'show'
            pa.show_actions()  # Show current and undone actions
        elif cmd:  # If user enters any other action
            pa.client_action(cmd)  # Log the action as performed
