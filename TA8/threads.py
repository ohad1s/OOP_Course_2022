import random
import threading
import time
from queue import Queue

class item():
    pass

class consumer():
    def __init__(self, control_room) -> None:
        self.control_room = control_room
    def consume(self):
        while True:
            time.sleep(random.randint(0,1000)/1000)
            element = self.control_room.get()
            print("Consumed! Queue size: {}".format(self.control_room.queue.qsize()))
            print()

class producer():
    def __init__(self, control_room) -> None:
        self.control_room = control_room
    def produce(self, item):
        while True:
            time.sleep(random.randint(0,1000)/1000)
            self.control_room.put(item)
            print("Produced! Queue size: {}".format(self.control_room.queue.qsize()))
            print()

class control_room():
    def __init__(self, maxsize) -> None:
        self.queue = Queue(maxsize)

    def get(self):
        return self.queue.get()

    def put(self, element):
        self.queue.put(element)

cr = control_room(5)
my_producer = producer(cr)
my_consumer = consumer(cr)
producer_t = threading.Thread(target=my_producer.produce, args=(item(),))
consumer_t = threading.Thread(target=my_consumer.consume)

producer_t.start()
consumer_t.start()

