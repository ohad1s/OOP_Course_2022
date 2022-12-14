# The Adaptee class contains the legacy code that needs to be adapted.
# In this example, the Adaptee class is a database driver that uses a
# legacy API for connecting to and querying a database.
class Adaptee:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        print(f"Connecting to {self.host}:{self.port} as user {self.user}")

    def query(self, sql):
        print(f"Querying database with SQL: {sql}")

# The Adapter class allows the Adaptee to be used by the new code.
# In this example, the Adapter class provides a new API for connecting
# to and querying a database, while using the Adaptee's legacy API
# under the hood.
class Adapter:
    def __init__(self, host, port, user, password):
        self.adaptee = Adaptee(host, port, user, password)

    def connect(self):
        self.adaptee.connect()

    def execute(self, sql):
        self.adaptee.query(sql)

# The Client class uses the Adapter to connect to and query a database.
class Client:
    def main(self):
        # Create an Adapter instance with the appropriate connection
        # parameters for the database.
        adapter = Adapter("localhost", 5432, "user1", "password")

        # Connect to the database using the Adapter's new API.
        adapter.connect()

        # Query the database using the Adapter's new API.
        adapter.execute("SELECT * FROM users")

# The main program creates a Client and calls its main method.
if __name__ == "__main__":
    client = Client()
    client.main()
