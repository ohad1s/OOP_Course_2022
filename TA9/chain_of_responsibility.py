"""
The chain of responsibility design pattern is a behavioral design pattern
that allows a request to be passed along a chain of objects until it is handled by one of the objects.
It can be used to handle requests in a flexible and decoupled way,
and can be particularly useful in systems with complex and dynamic behavior.
"""

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._can_handle_request(request):
            self._handle_request(request)
        elif self._successor is not None:
            self._successor.handle_request(request)

    def _can_handle_request(self, request):
        raise NotImplementedError

    def _handle_request(self, request):
        raise NotImplementedError

class ConcreteHandler1(Handler):
    def _can_handle_request(self, request):
        return 0 < request <= 10

    def _handle_request(self, request):
        print(f"ConcreteHandler1 handled request {request}")

class ConcreteHandler2(Handler):
    def _can_handle_request(self, request):
        return 10 < request <= 20

    def _handle_request(self, request):
        print(f"ConcreteHandler2 handled request {request}")

class ConcreteHandler3(Handler):
    def _can_handle_request(self, request):
        return 20 < request <= 30

    def _handle_request(self, request):
        print(f"ConcreteHandler3 handled request {request}")

# Client code
handler1 = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3()))
handler1.handle_request(5)  # Output: ConcreteHandler1 handled request 5
handler1.handle_request(15) # Output: ConcreteHandler2 handled request 15
handler1.handle_request(25) # Output: ConcreteHandler3 handled request 25
handler1.handle_request(40) # Output: ConcreteHandler3 handled request 25



"""
In this example, we have a Handler class that serves as a base class for concrete handler classes.
 The Handler class has a handle_request method that is responsible for deciding whether or not the current handler 
 can handle the request, and if not, passing the request along to the next handler in the chain.

We have three concrete handler classes: ConcreteHandler1, ConcreteHandler2, and ConcreteHandler3, which are responsible 
for handling requests in the range of 0-10, 10-20, and 20-30, respectively.

To use the chain of responsibility pattern, we create a chain of handlers by passing the next handler in the chain 
as an argument to the constructor of the current handler. In this example, we create a chain of handlers with ConcreteHandler1 
at the head, followed by ConcreteHandler2, and finally ConcreteHandler3.

To send a request through the chain of handlers, we call the handle_request method on the head of 
the chain, passing the request as an argument. The head of the chain will pass the request down the chain until it is
 handled by one of the concrete handlers.
"""
