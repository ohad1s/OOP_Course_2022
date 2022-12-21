"""
Open/Closed Principle (OCP): Software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification
"""

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def get_area(shape):
    return shape.area()


# In this example, the Shape class is open for extension
# (you can create new shapes by subclassing it), but closed for modification
#     (you don't need to modify the Shape class to add a new type of shape).