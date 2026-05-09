"""
Abstract Base Classes (ABC) and Interfaces.
Demonstrates the implementation of formal interfaces using the abc module.
"""

from abc import ABC, abstractmethod
from typing import List

class Shape(ABC):
    """Abstract base class representing a generic shape."""

    @abstractmethod
    def area(self) -> float:
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculates the perimeter of the shape."""
        pass

class Rectangle(Shape):
    """Concrete implementation of a Rectangle."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Concrete implementation of a Circle."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

def calculate_total_area(shapes: List[Shape]) -> float:
    """Polymorphic function that works with any Shape implementation."""
    return sum(shape.area() for shape in shapes)

if __name__ == "__main__":
    rect = Rectangle(10, 5)
    circ = Circle(7)
    
    shapes = [rect, circ]
    
    for shape in shapes:
        print(f"Type: {type(shape).__name__}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 20)

    print(f"Total Area of all shapes: {calculate_total_area(shapes):.2f}")
