"""
Standard Library Mastery: itertools and functools.
Covers efficient iteration and functional programming utilities.
"""

import itertools
import functools
from typing import List, Tuple

def get_permutations(data: List[int]) -> List[Tuple[int, ...]]:
    """Returns all permutations of a list using itertools."""
    return list(itertools.permutations(data))

def get_running_totals(data: List[int]) -> List[int]:
    """Returns accumulated sums using itertools.accumulate."""
    return list(itertools.accumulate(data))

@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """Calculates fibonacci numbers with memoization using lru_cache."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def multiply(a: int, b: int) -> int:
    """Base function for partial application."""
    return a * b

# Partial application: fix one argument
double = functools.partial(multiply, 2)

if __name__ == "__main__":
    # Itertools
    nums = [1, 2, 3]
    print(f"Permutations of {nums}: {get_permutations(nums)}")
    print(f"Running totals: {get_running_totals([10, 20, 30, 40])}")

    # Combinations
    print(f"Combinations (2 of 3): {list(itertools.combinations(nums, 2))}")

    # Functools
    print(f"\nFibonacci(50) (Efficient): {fibonacci(50)}")
    print(f"Partial Function (Double 21): {double(21)}")

    # Reduce example
    sum_all = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    print(f"Reduce Sum [1..5]: {sum_all}")
