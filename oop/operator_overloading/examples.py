# --- Content from operator overloading.py ---
# Python program to show use of
# + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Geeks" + "For")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks" * 4)


# --- Content from operatoroverloading.py ---
# Python Program illustrate how
# to overload an binary + operator
# And how it actually works


class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))
# And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))


# --- Content from operatoroverloading3.py ---
# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.


class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


# --- Content from operatoroverloading4.py ---
# Python program to overload
# a comparison operators


class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a > other.a:
            return True
        else:
            return False


ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")


# --- Content from operatoroverloading5.py ---
# Python program to overload equality
# and less than operators


class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)


# --- Content from operatoroverloading6.py ---
# Python program which attempts to
# overload ~ operator as binary operator


class A:
    def __init__(self, a):
        self.a = a

    # Overloading ~ operator, but with two operands
    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)

print(~ob1)


# --- Content from operatoroverloading7.py ---
class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)


a = MyClass(True)
b = MyClass(False)
c = a & b  # c.value is False
