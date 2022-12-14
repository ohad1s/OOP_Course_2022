import threading

class Database:
    __instance = None

    @staticmethod
    def get_instance():
        """
        The @staticmethod decorator is used in the Singleton
         class to indicate that the get_instance method is a static method.
         A static method is a method that belongs to a class rather than an instance of the class. \
         This means that it can be called on the class itself, rather than on an instance of the class.
        """
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self
            self.lock = threading.Lock()
            self.data = {}

    def insert(self, key, value):
        with self.lock:
            self.data[key] = value

    def update(self, key, value):
        with self.lock:
            if key in self.data:
                self.data[key] = value
            else:
                raise KeyError("Key not found in database")

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]
            else:
                raise KeyError("Key not found in database")

    def get(self, key):
        with self.lock:
            if key in self.data:
                return self.data[key]
            else:
                raise KeyError("Key not found in database")
db333=Database()
print(db333)
db1 = Database.get_instance()
db2 = Database.get_instance()
print(db333==db1)

# db1 and db2 are the same object
assert db1 == db2
print(db1 == db2)

# This will raise an exception, because the Database class is a singleton
# and only one instance can be created.
try:
    db3 = Database()
except Exception as e:
    print(e)

# Insert some data into the database
db1.insert("key1", "value1")
db1.insert("key2", "value2")

# Update a value in the database
db1.update("key1", "new_value1")

# Delete a value from the database
db1.delete("key2")

# Get a value from the database
print(db1.get("key1"))

# This will raise a KeyError, because the key has been deleted from the database
try:
    db1.get("key2")
except KeyError as e:
    print(e)
