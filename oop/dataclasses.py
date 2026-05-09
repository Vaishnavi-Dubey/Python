"""
Python Dataclasses (PEP 557).
Covers @dataclass, field, frozen, and post-initialization logic.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass(frozen=True)
class UserProfile:
    """An immutable user profile record."""
    username: str
    email: str
    joined_date: datetime = field(default_factory=datetime.now)

@dataclass
class Project:
    """A mutable project record with custom post-init logic."""
    name: str
    owner: str
    technologies: List[str] = field(default_factory=list)
    is_active: bool = True
    slug: str = field(init=False) # Not passed in __init__

    def __post_init__(self):
        """Logic to run after the generated __init__."""
        self.slug = self.name.lower().replace(" ", "-")

if __name__ == "__main__":
    # Create an immutable user
    user = UserProfile(username="vaishnavi", email="vaishnavi@example.com")
    print(f"User: {user}")
    
    # user.username = "new_name" # This would raise FrozenInstanceError

    # Create a mutable project
    proj = Project(
        name="AI Portfolio Optimizer", 
        owner="Vaishnavi",
        technologies=["Python", "PyTorch"]
    )
    print(f"Project: {proj}")
    print(f"Generated Slug: {proj.slug}")

    # Equality check (generated automatically)
    proj2 = Project(name="AI Portfolio Optimizer", owner="Vaishnavi", technologies=["Python", "PyTorch"])
    print(f"Projects Equal? {proj == proj2}")
