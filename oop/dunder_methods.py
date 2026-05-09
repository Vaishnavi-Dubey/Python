"""
Advanced Object Oriented Programming: Dunder Methods.
Covers lifecycle, representation, container, and operator dunder methods.
"""

from typing import Any, List

class SmartVector:
    """A 2D vector class demonstrating various magic (dunder) methods."""

    def __init__(self, x: float, y: float):
        """Initializes the vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Developer-focused string representation."""
        return f"SmartVector(x={self.x}, y={self.y})"

    def __add__(self, other: 'SmartVector') -> 'SmartVector':
        """Allows vector addition using the + operator."""
        if not isinstance(other, SmartVector):
            raise TypeError("Can only add SmartVector to SmartVector")
        return SmartVector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Any) -> bool:
        """Allows equality check using the == operator."""
        if not isinstance(other, SmartVector):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        """Returns the 'dimension' of the vector (always 2 for this class)."""
        return 2

class SkillList:
    """A container class demonstrating iteration and membership dunder methods."""

    def __init__(self, skills: List[str]):
        self._skills = skills

    def __iter__(self):
        """Allows the object to be used in a for-loop."""
        return iter(self._skills)

    def __contains__(self, item: str) -> bool:
        """Allows usage of the 'in' keyword."""
        return item in self._skills

if __name__ == "__main__":
    v1 = SmartVector(3, 4)
    v2 = SmartVector(1, 2)
    v3 = v1 + v2

    print(f"v1: {v1}")
    print(f"v2: {v2!r}") # Calls __repr__
    print(f"v1 + v2 = {v3}")
    print(f"v1 == v2? {v1 == v2}")
    print(f"Dimension of v1: {len(v1)}")

    my_skills = SkillList(["Python", "Machine Learning", "DevOps"])
    print("\nIterating through SkillList:")
    for skill in my_skills:
        print(f"- {skill}")
    
    print(f"Is 'Python' in my_skills? {'Python' in my_skills}")
