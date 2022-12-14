# The Strategy class defines the interface for all concrete strategies.
class Strategy:
    def do_algorithm(self, data):
        pass

# The ConcreteStrategyA class implements the Strategy interface for a
# specific algorithm.
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        # Implement algorithm A
        print("Using algorithm A on data:", data)

# The ConcreteStrategyB class implements the Strategy interface for a
# specific algorithm.
class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        # Implement algorithm B
        print("Using algorithm B on data:", data)

# The Context class maintains a reference to a Strategy and allows
# clients to execute the algorithm defined by the Strategy.
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_algorithm(self, data):
        self.strategy.do_algorithm(data)

# The Client class uses the Context to execute an algorithm defined by
# a concrete Strategy.
class Client:
    def main(self):
        # Create a Context with a ConcreteStrategyA.
        context = Context(ConcreteStrategyA())
        # Execute the algorithm using the ConcreteStrategyA.
        context.execute_algorithm("ABC123")

        # Create a Context with a ConcreteStrategyB.
        context = Context(ConcreteStrategyB())
        # Execute the algorithm using the ConcreteStrategyB.
        context.execute_algorithm("ABC123")

# The main program creates a Client and calls its main method.
if __name__ == "__main__":
    client = Client()
    client.main()
