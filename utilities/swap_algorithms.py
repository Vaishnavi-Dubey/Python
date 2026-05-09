# --- Content from 5_swap.py ---
P = int(input("Enter the value of P "))
Q = int(input("Enter the value of Q "))

# To swap the value of two variables
# we will user third variable which is a temporary variable
temp_1 = P
P = Q
Q = temp_1

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)


# --- Content from 6_swap2.py ---
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To Swap the values of two variables
P, Q = Q, P

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)

# --- Content from 7_ swap3.py ---
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To Swap the values of two variables using XOR
P = P ^ Q
Q = P ^ Q
P = P ^ Q

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)

# --- Content from 8_swap4.py ---
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To Swap the values of two variables using Addition and subtraction operator
P = P + Q
Q = P - Q
P = P - Q

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)

# --- Content from 9_swap5.py ---
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To Swap the values of two variables using Addition and subtraction operator
P = P * Q
Q = P / Q
P = P / Q

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q)
