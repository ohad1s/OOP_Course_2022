import time

class Observer:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)

    def __repr__(self) -> str:
        return "Fabrizio Romano"

class StockObserver:
    def __init__(self, name):
        self.name = name

    def notify(self, observable, *args, **kwargs):
        print("{} received notification from {}: args = {}, kwargs = {}".format(
            self.name, observable, args, kwargs))

# Create an Observer instance
stock_observer = StockObserver("Yoni")
stock_observer2 = StockObserver("Yossi")
stock_observer3 = StockObserver("Dani")
stock_observer4 = StockObserver("Dana")
stock_observer5 = StockObserver("Ben")

# Create an Observer instance and register the observer
observer = Observer()
observer.register(stock_observer)
observer.register(stock_observer2)
observer.register(stock_observer3)
observer.register(stock_observer4)
observer.register(stock_observer5)

# Notify the observer of a change
observer.notify_observers("Player signed in a team!", player="Cristiano Ronaldo", team="El Nasser")
time.sleep(1)
observer.notify_observers("Coach fired!", player="Elyaniv Barda", team="Hapoel Beer Sheva")
