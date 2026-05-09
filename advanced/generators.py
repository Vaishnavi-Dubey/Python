"""
Python Generators and Iterators.
Covers yield, send, and generator pipelines for memory-efficient processing.
"""

from typing import Generator, List

def infinite_sequence() -> Generator[int, None, None]:
    """An infinite generator for positive integers."""
    num = 1
    while True:
        yield num
        num += 1

def power_generator(nums: List[int]) -> Generator[int, None, None]:
    """Yields squares of numbers from a list."""
    for n in nums:
        yield n ** 2

def csv_line_reader(file_content: List[str]) -> Generator[str, None, None]:
    """Simulates reading lines from a large file lazily."""
    for line in file_content:
        yield line.strip()

def filter_logs(lines: Generator[str, None, None], keyword: str) -> Generator[str, None, None]:
    """A generator pipeline component that filters lines by a keyword."""
    for line in lines:
        if keyword in line:
            yield line

if __name__ == "__main__":
    # 1. Simple Generator
    print("Squares:")
    for square in power_generator([1, 2, 3, 4]):
        print(square, end=" ")
    print("\n")

    # 2. Infinite Sequence (Limited)
    print("First 5 of infinite sequence:")
    gen = infinite_sequence()
    for _ in range(5):
        print(next(gen), end=" ")
    print("\n")

    # 3. Generator Pipeline
    print("Log Filtering Pipeline:")
    raw_logs = [
        "INFO: System Start",
        "ERROR: Null Pointer",
        "INFO: User Login",
        "ERROR: Disk Full"
    ]
    
    # Building the pipeline
    lines = csv_line_reader(raw_logs)
    errors = filter_logs(lines, "ERROR")
    
    for err in errors:
        print(f"Detected: {err}")
