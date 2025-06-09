
import threading


class ReaderWriterLock:
    def __init__(self):
        self.readers = 0
        self.lock = threading.Lock()
        self.read_ready = threading.Condition(self.lock)

    def acquire_read(self):
        with self.lock:
            self.readers += 1

    def release_read(self):
        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.read_ready.notify_all()

    def acquire_write(self):
        self.lock.acquire()
        while self.readers > 0:
            self.read_ready.wait()

    def release_write(self):
        self.lock.release()


# Example usage:
# rw_lock = ReaderWriterLock()
# rw_lock.acquire_read()
# ... read data ...
# rw_lock.release_read()
# rw_lock.acquire_write()
# ... write data ...
# rw_lock.release_write()
