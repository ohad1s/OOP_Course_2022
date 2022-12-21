"""
Single Responsibility Principle (SRP):
A class or function should have a single, well-defined responsibility
"""
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

class UserRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save(self, user):
        # Save the user to the database using the connection string
        pass

# In this example, the User class has a single responsibility:
#     storing and providing access to a
#     user's name and email. The UserRepository class has a single responsibility:
#         saving a user to the database.