# --- Content from import.py ---
# import keyword
import math
from math import factorial

print(math.factorial(10))

# from keyword
print(factorial(10))


# --- Content from as_examples.py ---
import math as m

print(m.factorial(5))


# --- Content from with_examples.py ---
# using with statement
with open("file_path", "w") as file:
    file.write("hello world !")


# --- Content from del_examples.py ---
my_variable1 = 20
my_variable2 = "wakattadattebayo"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete both the variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)
