import cmath
import math
from typing import Tuple, Union

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_triangle_area(a: float, b: float, c: float) -> float:
    """Calculates the area of a triangle using Heron's formula."""
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def solve_quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """Solves a quadratic equation ax^2 + bx + c = 0."""
    d = (b**2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return sol1, sol2

def main():
    # Example usage
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        print(f"Sum: {add(n1, n2)}")
        print(f"Product: {multiply(n1, n2)}")
        
        a = float(input("Enter triangle side a: "))
        b = float(input("Enter triangle side b: "))
        c = float(input("Enter triangle side c: "))
        print(f"Triangle Area: {calculate_triangle_area(a, b, c):.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
