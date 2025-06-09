import threading


class NotThreadSafeQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def count(self):
        return len(self.data)


# Usage with caller synchronization:
queue = NotThreadSafeQueue()
lock = threading.Lock()


def process_next_job():
    # 1. Check if the count is more than 0 while outside the lock
    if queue.count() > 0:
        # 2. Take the lock
        with lock:
            # 3. Check the count again while under the lock
            if queue.count() > 0:
                # 4. While holding the lock, Dequeue the next job
                job = queue.dequeue()
            else:
                job = None
    else:
        job = None

    # 5. If we dequeued a job, then process it
    if job is not None:
        process_job(job)


def process_job(job):
    # Placeholder for job processing logic
    print(f"Processing job: {job}")


# Example usage:
# queue.enqueue("Job1")
# process_next_job()
