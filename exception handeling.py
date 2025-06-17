# initializing number
a = 4
b = 0

# No exception Exception raised in try block
try:
    k = a // b  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

# assert Keyword
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print(a / b)

# raise keyword
# Raises an user defined exception
# if strings are not equal
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")
