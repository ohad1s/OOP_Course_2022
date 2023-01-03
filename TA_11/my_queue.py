import threading
class MyQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.queue.append(item)

    def put_2(self, item):
        self.lock.acquire()
        try:
            self.queue.append(item)
        finally:
            self.lock.release()

    def get(self):
        with self.lock:
            return self.queue.pop(0)

    def get_2(self):
        self.lock.acquire()
        try:
            return self.queue.pop(0)
        finally:
            self.lock.release()