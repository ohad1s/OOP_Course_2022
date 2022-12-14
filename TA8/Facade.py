# The Facade class defines a new, simplified interface for the complex
# system. It maintains references to the classes that make up the complex
# system, and it delegates client requests to the appropriate classes.
class Facade: #### Library is a good example for that
    def __init__(self):
        self.class1 = Class1()
        self.class2 = Class2()

    def operation(self, data):
        result1 = self.class1.operation1(data)
        result2 = self.class1.operation2()
        result3 = self.class2.operation1(result1, result2)
        result4 = self.class2.operation2(result3)
        return result4

# The Class1 and Class2 classes are part of the complex system. They
# define the operations that the Facade can delegate to.
class Class1:
    def operation1(self, data):
        print("Class1 operation1:", data)
        return data.upper()

    def operation2(self):
        print("Class1 operation2")
        return "hello"

class Class2:
    def operation1(self, data1, data2):
        print("Class2 operation1:", data1, data2)
        return data1 + " " + data2

    def operation2(self, data):
        print("Class2 operation2:", data)
        return data.split()

    # The Client class uses the Facade to access the functionality of the
    # complex system.


class Client:
    def main(self):
        # Create a Facade and use it to access the complex system.
        facade = Facade()
        result = facade.operation("abc123")
        print("Result:", result)

    # The main program creates a Client and calls its main method.


if __name__ == "__main__":
    client = Client()
    client.main()



