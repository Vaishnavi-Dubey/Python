"""
Advanced Python Decorators.
Covers function decorators, parameterized decorators, and class-based decorators.
"""

import functools
import time
from typing import Callable, Any

def timer_decorator(func: Callable) -> Callable:
    """A decorator that measures the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time:.4f}s")
        return result
    return wrapper

def repeat(num_times: int) -> Callable:
    """A parameterized decorator that repeats a function call."""
    def decorator_repeat(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

class CountCalls:
    """A class-based decorator that counts function calls."""
    def __init__(self, func: Callable):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Any:
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@timer_decorator
@repeat(num_times=2)
def complex_operation(name: str) -> None:
    """A dummy operation to demonstrate stacked decorators."""
    print(f"Hello {name}, performing heavy task...")
    time.sleep(0.5)

@CountCalls
def say_hello() -> None:
    """A function decorated by a class."""
    print("Hello!")

if __name__ == "__main__":
    print("Testing Stacked Decorators:")
    complex_operation("Vaishnavi")
    
    print("\nTesting Class Decorator:")
    say_hello()
    say_hello()
