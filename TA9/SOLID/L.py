"""
Liskov Substitution Principle (LSP):
Subtypes must be substitutable for their base types
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side


# In this example, the Square class is a subtype of the Rectangle class,
# and it should be substitutable for Rectangle objects.This means that any code that expects
# a Rectangle should be able to work with a Square without any problems