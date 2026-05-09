import pytest
from utilities.math_operations import add, subtract, multiply, divide, calculate_triangle_area

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_triangle_area():
    # Right triangle 3, 4, 5 should have area 6
    assert calculate_triangle_area(3, 4, 5) == 6.0
