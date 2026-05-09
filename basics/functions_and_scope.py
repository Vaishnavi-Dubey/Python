from typing import Generator, Any

def get_integer() -> int:
    """Prompts the user for an integer and returns it."""
    try:
        result = int(input("Enter integer: "))
        return result
    except ValueError:
        print("Invalid input! Defaulting to 0.")
        return 0

def hello_world() -> None:
    """Prints a simple hello message."""
    print("Hello from a function!")

# Lambda examples
square = lambda x: x * x
cube = lambda x: x ** 3

def sum_up_to(n: int) -> int:
    """Calculates the sum of numbers from 0 to n-1 using a return statement."""
    s = 0
    for i in range(n):
        s += i
    return s

def generator_sum(n: int) -> Generator[int, None, None]:
    """Yields a running sum from 0 to n-1."""
    s = 0
    for i in range(n):
        s += i
        yield s

# Global and Nonlocal examples
count = 5

def update_global():
    global count
    count += 1
    print(f"Updated global count: {count}")

def outer_function():
    var1 = 10
    def inner_function():
        nonlocal var1
        var1 += 10
        print(f"Updated nonlocal var1: {var1}")
    inner_function()

def main():
    print("--- Function Examples ---")
    hello_world()
    
    val = 7
    print(f"Square of {val}: {square(val)}")
    print(f"Cube of {val}: {cube(val)}")
    
    print(f"Sum up to 10: {sum_up_to(10)}")
    
    print("Generator output:")
    for s in generator_sum(5):
        print(s, end=" ")
    print()
    
    update_global()
    outer_function()

if __name__ == "__main__":
    main()
