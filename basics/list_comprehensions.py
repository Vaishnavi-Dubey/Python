"""
Comprehensive guide to Python Comprehensions.
Covers List, Dictionary, Set, and Generator comprehensions with practical examples.
"""

from typing import List, Dict, Set, Generator

def get_squares(numbers: List[int]) -> List[int]:
    """Returns a list of squares using list comprehension."""
    return [x**2 for x in numbers]

def get_even_squares(numbers: List[int]) -> List[int]:
    """Returns a list of squares of even numbers using list comprehension with conditional."""
    return [x**2 for x in numbers if x % 2 == 0]

def get_name_length_map(names: List[str]) -> Dict[str, int]:
    """Returns a dictionary mapping names to their lengths using dict comprehension."""
    return {name: len(name) for name in names}

def get_unique_vowels(text: str) -> Set[str]:
    """Returns a set of unique vowels in a string using set comprehension."""
    return {char.lower() for char in text if char.lower() in 'aeiou'}

def get_lazy_squares(n: int) -> Generator[int, None, None]:
    """Returns a generator comprehension for squares up to n."""
    return (x**2 for x in range(n))

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    names = ["Alice", "Bob", "Charlie"]
    text = "The quick brown fox jumps over the lazy dog"

    print(f"Original Numbers: {nums}")
    print(f"Squares: {get_squares(nums)}")
    print(f"Even Squares: {get_even_squares(nums)}")
    
    print(f"\nName Lengths: {get_name_length_map(names)}")
    print(f"Unique Vowels: {get_unique_vowels(text)}")
    
    print("\nGenerator Comprehension (Lazy Evaluation):")
    gen = get_lazy_squares(5)
    for val in gen:
        print(val, end=" ")
    print()
