from queue import Queue

class Tasks:
    def __init__(self):
        self.task_queue = Queue()

    def add_task(self, task):
        self.task_queue.put(task)

    def execute_task(self):
        if self.is_empty():
            raise IndexError('No tasks to execute')
        return self.task_queue.get()

    def is_empty(self):
        return self.task_queue.empty()

    def task_count(self):
        return self.task_queue.qsize()
