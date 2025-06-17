# Define the data to be evaluated
data = [3, 5, 2, 8, 4]
# Use a for loop to evaluate each element in the data
for num in data:
    # Use the ternary operator to determine if the number is even or odd
    result = 'even' if num % 2 == 0 else 'odd'
    # Optionally, print the result of the ternary operator for each element
    print(f'The number {num} is {result}.')
