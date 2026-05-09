

# --- Content from input.py ---
val = input("Enter your value: ")
print(val)


# --- Content from input1.py ---
name = input('What is your name?\n')  # \n ---> newline ---> It causes a line break
print(name)


# --- Content from input2.py ---
# check input type in Python

num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))


# --- Content from input3.py ---
# Python program showing
# a use of raw_input()

g = raw_input("Enter your name : ")
print(g)


# --- Content from input4.py ---
num = int(input("Enter a number: "))
print(num, " ", type(num))

floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))


# --- Content from input5.py ---
# input
input1 = input()

# output
print(input1)


# --- Content from input6.py ---
# input
num1 = int(input())
num2 = int(input())

# printing the sum in integer
print(num1 + num2)


# --- Content from input7.py ---
# input
num1 = float(input())
num2 = float(input())

# printing the sum in float
print(num1 + num2)


# --- Content from input8.py ---
# input
string = str(input())

# output
print(string)

# Or by default
string_default = input()

# output
print(string_default)


# --- Content from input9.py ---
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)


# --- Content from input10.py ---
# Python program showing how to take multiple input using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)


# --- Content from input11.py ---
# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)


# --- Content from input12.py ---
name = input("Enter your name: ")

print("hello", name)


# --- Content from input13.py ---
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)
