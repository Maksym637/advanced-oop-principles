import math
from typing import List
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        pass


class AreaCalculator(Visitor):
    def visit_circle(self, circle: Circle):
        return math.pi * circle.radius**2

    def visit_rectangle(self, rectangle: Rectangle):
        return rectangle.width * rectangle.height


class Renderer(Visitor):
    def visit_circle(self, circle: Circle):
        return f"Drawing a circle with radius {circle.radius}"

    def visit_rectangle(self, rectangle: Rectangle):
        return f"Drawing a rectangle {rectangle.width}x{rectangle.height}"


shapes: List[Shape] = [Circle(5), Rectangle(4, 6), Circle(2)]

area_visitor = AreaCalculator()
render_visitor = Renderer()

for shape in shapes:
    print("<>" * 20)
    print(f"Area: {shape.accept(area_visitor)}")
    print(f"Render: {shape.accept(render_visitor)}")

print("<>" * 20)
