"""Dependency Inversion Principle (DIP):
High-level modules should not depend on low-level modules. Both should depend on abstractions"""

class Database:
    def save(self, data):
        # Save the data to the database
        pass

class FileSystem:
    def save(self, data, filename):
        with open(filename, 'w') as f:
            f.write(data)

class DataExporter:
    def __init__(self, storage):
        self.storage = storage

    def export(self, data):
        self.storage.save(data)

database = Database()
exporter = DataExporter(database)
exporter.export("some data")

filesystem = FileSystem()
exporter = DataExporter(filesystem)
exporter.export("data.txt")


# In this example, the DataExporter class depends on an abstraction (the storage parameter),
# rather than a specific implementation (like the Database or FileSystem classes). This allows the DataExporter to work with
#     any storage implementation, as long as it has a save method.