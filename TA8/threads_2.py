import random
import threading
import time

class item():
    pass

class consumer():
    def __init__(self, control_room) -> None:
        self.control_room = control_room
    def consume(self):
        while True:
            time.sleep(random.randint(0,1000)/1000)
            element = self.control_room.get()
            print("Consumed! Queue size: {}".format(self.control_room.size()))

class producer():
    def __init__(self, control_room) -> None:
        self.control_room = control_room
    def produce(self, item):
        while True:
            time.sleep(random.randint(0,1000)/1000)
            self.control_room.put(item)
            print("Produced! Queue size: {}".format(self.control_room.size()))

class control_room():
    def __init__(self, maxsize) -> None:
        self.queue = []
        self.lock = threading.Lock()
        self.empty_cond = threading.Condition(self.lock)
        self.full_cond = threading.Condition(self.lock)
        self.maxsize = maxsize

    def get(self):
        with self.lock:
            while len(self.queue) == 0:
                self.empty_cond.wait()
            element = self.queue.pop(0)
            self.full_cond.notify()
            return element

    def put(self, element):
        with self.lock:
            while len(self.queue) == self.maxsize:
                self.full_cond.wait()
            self.queue.append(element)
            self.empty_cond.notify()


    def size(self):
        with self.lock:
            return len(self.queue)

cr = control_room(5)
my_producer = producer(cr)
my_consumer = consumer(cr)
producer_t = threading.Thread(target=my_producer.produce, args=(item(),))
consumer_t = threading.Thread(target=my_consumer.consume)

producer_t.start()
consumer_t.start()
