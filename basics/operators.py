# --- Content from and or not in.py ---
# or (returns True)
print(True or False)

# and (returns False)
print(False and True)

# not (returns False)
print(not True)

# using "in" to check
if "s" in "geeksforgeeks":
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in "geeksforgeeks":
    print(i, end=" ")

print("\r")

# using is to check object identity string is immutable( cannot be changed once allocated) hence occupy same memory location
print(" " is " ")

# using is to check object identity dictionary is mutable( can be changed once allocated) hence occupy different memory location
print({} is {})


# --- Content from is keyword.py ---
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


# --- Content from membership.py ---
# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if x not in list:
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if y in list:
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# --- Content from operator_examples.py ---
# python program to demonstrate the use of "/"
print(5 / 5)
print(10 / 2)
print(-10 / 2)
print(20.0 / 2)


# --- Content from operator2.py ---
# python program to demonstrate the use of "//"
print(10 // 3)
print(-5 // 2)
print(5.0 // 2)
print(-5.0 // 2)


# --- Content from operator3.py ---
# Examples of Arithmetic Operator
a = 9
b = 4

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Modulo of both number
mod = a % b

# Power
p = a**b

# print results
print(add)
print(sub)
print(mul)
print(mod)
print(p)


# --- Content from operator4.py ---
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)


# --- Content from operator5.py ---
# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)


# --- Content from operator6.py ---
# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


# --- Content from operator7.py ---
# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)


# --- Content from operator8.py ---
a = 10
b = 20
c = a

print(a is not b)
print(a is c)


# --- Content from operator10.py ---
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)


# --- Content from operator11.py ---
# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


# --- Content from operator12.py ---
# Examples of Operator Associativity

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2**3**2)


# --- Content from operator13.py ---
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)


# --- Content from operator14.py ---
# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print((b, a)[a < b])

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({True: a, False: b}[a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())


# --- Content from operator15.py ---
# Python program to demonstrate nested ternary operator
a, b = 10, 20

print(
    "Both a and b are equal"
    if a == b
    else "a is greater than b" if a > b else "b is greater than a"
)


# --- Content from operator16.py ---
# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")


# --- Content from operator17.py ---
a = 5
b = 7

# [statement_on_True] if [condition] else [statement_on_false]

print(a, "is greater") if (a > b) else print(b, "is Greater")


# --- Content from operator18.py ---
# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)


# --- Content from operator19.py ---
# Define the data to be evaluated
data = [3, 5, 2, 8, 4]
# Use a for loop to evaluate each element in the data
for num in data:
    # Use the ternary operator to determine if the number is even or odd
    result = "even" if num % 2 == 0 else "odd"
    # Optionally, print the result of the ternary operator for each element
    print(f"The number {num} is {result}.")
