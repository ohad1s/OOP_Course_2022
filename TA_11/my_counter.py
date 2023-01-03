import threading

class Counter:
    def __init__(self):
        self.count = 0
        self.condition = threading.Condition()

    def __repr__(self) -> str:
        return str(self.count)

    def increment(self):
        with self.condition:
            self.count += 1
            self.condition.notify()

    def decrement(self):
        with self.condition:
            if self.count == 0:
                self.condition.wait()
            self.count -= 1

    def increment_2(self):
        self.condition.acquire()
        try:
            self.count += 1
            self.condition.notify()
        finally:
            self.condition.release()

    def decrement_2(self):
        self.condition.acquire()
        try:
            if self.count == 0:
                self.condition.wait()
            self.count -= 1
        finally:
            self.condition.release()

