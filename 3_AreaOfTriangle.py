# input 3 sides of the triangle
a=float(input("Enter first side"))
b=float(input("Enter second side"))
c=float(input("Enter third side"))

# calculate semi perimeter
s=(a+b+c)/2

# calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5

print('The area of triangle is %0.2f'%area)
