

# --- Content from function.py ---
def getInteger():


    result = int(input("Enter integer: "))
return result


def Main():


    print("Started")

output = getInteger()
print(output)

if __name__ == "__main__":
    Main()


# --- Content from functions.py ---
def hello():


    print("hello")
print("hello again")
hello()

hello()


# --- Content from lambda.py ---
# Lambda keyword
g = lambda x: x * x * x

print(g(7))


# --- Content from return.py ---
# Return keyword
def fun():
    S = 0

    for i in range(10):
        S += i
    return S


print(fun())


# Yield Keyword


def fun():
    S = 0

    for i in range(10):
        S += i
        yield S


for i in fun():
    print(i)


# --- Content from global variable.py ---
# Python program processing
# global variable

count = 5


def some_method():
    global count
    count = count + 1
    print(count)


some_method()


# --- Content from gobal nonlocal.py ---
# global variable
a = 15
b = 10


# function to perform addition
def add():
    c = a + b
    print(c)


# calling a function
add()


# nonlocal keyword
def fun():
    var1 = 10

    def gun():
        # tell python explicitly that it
        # has to access var1 initialized
        # in fun on line 2
        # using the keyword nonlocal
        nonlocal var1

        var1 = var1 + 10
        print(var1)

    gun()


fun()


# --- Content from namespace.py ---
# var1 is in the global namespace
var1 = 5


def some_func():
    # var2 is in the local namespace
    var2 = 6

    def some_inner_func():
        # var3 is in the nested local
        # namespace
        var3 = 7


# --- Content from scope.py ---
# a scope of object

def some_func():
    print("Inside some_func")

    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:", var)

    some_inner_func()
    print("Try printing var from outer function: ", var)


some_func()


# --- Content from def_examples.py ---
# def keyword
def fun():
    print("Inside Function")


fun()
