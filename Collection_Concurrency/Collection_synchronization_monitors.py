import threading


class MonitorQueue:
    def __init__(self, maxsize=10):
        self.queue = []
        self.maxsize = maxsize
        self.condition = threading.Condition()  # Monitor for synchronization

    def put(self, item):
        with self.condition:  # Enter monitor (acquire lock)
            while len(self.queue) >= self.maxsize:
                self.condition.wait()  # Wait until space is available
            self.queue.append(item)
            self.condition.notify_all()  # Notify waiting threads

    def get(self):
        with self.condition:  # Enter monitor (acquire lock)
            while not self.queue:
                self.condition.wait()  # Wait until item is available
            item = self.queue.pop(0)
            self.condition.notify_all()  # Notify waiting threads
            return item


# Example usage:
# q = MonitorQueue(maxsize=5)
# Thread 1: q.put(x)
# Thread 2: q.get()
