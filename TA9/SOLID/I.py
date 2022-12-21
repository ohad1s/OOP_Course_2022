"""
Interface Segregation Principle (ISP):
Clients should not be forced to depend on interfaces they do not use
"""

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        # Draw a circle
        pass

class Rectangle(Shape):
    def draw(self):
        # Draw a rectangle
        pass

class Triangle(Shape):
    def draw(self):
        # Draw a triangle
        pass

def draw_shapes(shapes):
    for shape in shapes:
        shape.draw()

class AdvancedShape(Shape):
    def draw_outline(self):
        # Draw the outline of the shape
        pass

class AdvancedCircle(Circle, AdvancedShape):
    def draw_outline(self):
        # Draw the outline of a circle
        pass

def draw_outlines(shapes):
    for shape in shapes:
        if isinstance(shape, AdvancedShape):
            shape.draw_outline()


# In this example, the AdvancedShape interface defines an additional method,
# draw_outline, that is not required by the base Shape interface. This means that a client
# that only needs to draw basic shapes (like the draw_shapes function) should not be forced
# to depend on the AdvancedShape interface