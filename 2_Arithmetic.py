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
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
print('The division of {0} and {1} is {2}'.format(num1, num2, div))
