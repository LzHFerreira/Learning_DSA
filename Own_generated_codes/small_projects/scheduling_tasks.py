# Going to simulate a task scheduling system, just to implement a priority queue
from queue import Queue  # Import the Queue class from the queue module


class Tasks:
    def __init__(self):
        # Initialize an empty queue to store tasks
        self.task_queue = Queue()  # Create a new Queue object to hold tasks

    def add_task(self, task):
        # Add a task to the queue
        self.task_queue.put(task)  # Put the given task into the queue

    def execute_task(self):
        # Execute and remove the task from the queue
        if self.is_empty():  # Check if the queue is empty before executing
            raise IndexError("No tasks to execute")  # Raise an error if empty
        return self.task_queue.get()  # Remove and return the next task in the queue

    def is_empty(self):
        # Check if there are no tasks in the queue
        return self.task_queue.empty()  # Return True if the queue is empty

    def task_count(self):
        # Return the number of tasks in the queue
        return self.task_queue.qsize()  # Return the current size of the queue


if __name__ == "__main__":
    task_manager = Tasks()  # Create an instance of the Tasks class

    while True:  # Start an infinite loop for CLI interaction
        command = (
            input(
                "Enter 'add' to add a task, 'execute' to execute a task, 'count' to check tasks, or 'q' to quit: "
            )
            .strip()  # Remove leading/trailing whitespace from input
            .lower()  # Convert input to lowercase for easier comparison
        )

        if command == "q":  # If the user wants to quit
            print("Exiting the task manager.")  # Print exit message
            break  # Exit the loop and end the program
        elif command == "add":  # If the user wants to add a task
            task = input("Enter the task description: ")  # Prompt for task description
            task_manager.add_task(task)  # Add the task to the queue
            print(f"Task '{task}' added.")  # Confirm task addition
        elif command == "execute":  # If the user wants to execute a task
            try:
                executed_task = task_manager.execute_task()  # Try to execute the next task
                print(f"Executed task: {executed_task}")  # Print the executed task
            except IndexError as e:  # If there are no tasks to execute
                print(e)  # Print the error message
        elif command == "count":  # If the user wants to check the number of tasks
            print(f"Number of tasks in the queue: {task_manager.task_count()}")  # Print the task count
        else:
            print("Invalid command. Please try again.")  # Handle invalid commands
