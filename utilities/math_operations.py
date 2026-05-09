# --- Content from 2_Arithmetic.py ---
# store input numbers
num1 = input("Enter first number")
num2 = input("enter second number")

# add two numbers
sum = float(num1) + float(num2)

# subtract two numbers
min = float(num1) - float(num2)

# multiply two numbers
mul = float(num1) * float(num2)

# divide
div = float(num1) / float(num2)

# display
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
print("The subtraction of {0} and {1} is {2}".format(num1, num2, min))
print("The multiplication of {0} and {1} is {2}".format(num1, num2, mul))
print("The division of {0} and {1} is {2}".format(num1, num2, div))


# --- Content from 3_AreaOfTriangle.py ---
# input 3 sides of the triangle
a = float(input("Enter first side"))
b = float(input("Enter second side"))
c = float(input("Enter third side"))

# calculate semi perimeter
s = (a + b + c) / 2

# calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The area of triangle is %0.2f" % area)


# --- Content from 4_QuadraticEquation.py ---
# import complex math module
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate the discriminant
d = (b**2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print("The solution are {0} and {1}".format(sol1, sol2))

# --- Content from math module.py ---
import math


def Main():
    num = -85


num = math.fabs(num)
print(num)

if __name__ == "__main__":
    Main()
