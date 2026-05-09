"""
Comprehensive Python Type Hinting (PEP 484/585).
Covers basic annotations, Optional, Union, Any, and Generic protocols.
"""

from typing import (
    List, 
    Dict, 
    Tuple, 
    Optional, 
    Union, 
    Any, 
    Callable, 
    TypeVar, 
    Sequence,
    Protocol
)

# 1. Basic and Complex Aliases
UserId = int
Point = Tuple[float, float]

# 2. Generics
T = TypeVar("T") # Can be any type

def get_first_element(elements: Sequence[T]) -> Optional[T]:
    """Returns the first element of a sequence, or None if empty."""
    return elements[0] if elements else None

# 3. Protocols (Structural Subtyping / Interfaces)
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str: return "Drawing a Circle"

class Square:
    def draw(self) -> str: return "Drawing a Square"

def render(shape: Drawable) -> None:
    """Accepts any object that implements the 'draw' method."""
    print(shape.draw())

# 4. Functional Types
def apply_operation(val: int, func: Callable[[int], int]) -> int:
    """Applies a transformation function to a value."""
    return func(val)

if __name__ == "__main__":
    # Generic usage
    names: List[str] = ["Alice", "Bob"]
    first_name = get_first_element(names)
    print(f"First Name: {first_name}")

    # Union and Optional
    def process_data(data: Union[str, int, None]) -> str:
        if data is None:
            return "No data"
        return str(data)

    print(f"Processed: {process_data(100)}")
    print(f"Processed: {process_data(None)}")

    # Protocol usage
    render(Circle())
    render(Square())

    # Callable usage
    result = apply_operation(5, lambda x: x * 10)
    print(f"Operation Result: {result}")
