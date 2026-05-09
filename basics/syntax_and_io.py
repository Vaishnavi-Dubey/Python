

# --- Content from print_examples.py ---
# Script Begins

print("Wakattadattebayo")

# Scripts Ends


# --- Content from print1.py ---
print("onii"),
print("onigiri")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in xrange(4):
    print(a[i]),


# --- Content from print2.py ---
print("oni", end=" ")
print("onigiri")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
    print(a[i], end=" ")


# --- Content from print3.py ---
l = [1, 2, 3, 4, 5, 6]

# using * symbol prints the list
# elements in a single line
print(*l)


# --- Content from print4.py ---
import sys

sys.stdout.write("hello ")
sys.stdout.write("jeee")


# --- Content from output.py ---
print("anime \n is best for story Content.")


# --- Content from output2.py ---
print("anime is the best platform for story content")

# This print() function ends with "**" as set in the end argument.
print("hehe is the best for content", end="**")
print("Welcome to anime")


# --- Content from output3.py ---
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')


# --- Content from output4.py ---
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush=True)
        time.sleep(1)
    else:
        print('Start')


# --- Content from output5.py ---
import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello jeee!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()


# --- Content from output6.py ---
print('Welcome to one piece wakattadattebayo.!!', file=open('Testfile.txt', 'w'))


# --- Content from output7.py ---
# One object is passed
print("hehe")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('h', 'e', 'h', sep='')

# using end argument
print("Python", end='@')
print("heh")


# --- Content from format.py ---
# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format() method and referring
# a position of the object
print(f"{'Geeks'} and {'Portal'}")


# --- Content from format3.py ---
# Python program showing
# a use of format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
      .format('Geeks', 'For', other='Geeks'))

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
      format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d}, Portal: {p:8.2f}".
      format(a=453, p=59.058))


# --- Content from format4.py ---
# Python program to
# show format() is
# used in dictionary

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
      'Geeks: {0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))


# --- Content from format5.py ---
# Python program to
# format a output using
# string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print("The left aligned string is : ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print("The right aligned string is : ")
print(cstr.rjust(40, '-'))


# --- Content from formatting.py ---
# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))


# --- Content from sep parameter.py ---
print('h', 'e', sep='', end='')
print('h')
# \n provides new line after printing the year
print('09', '12', '2016', sep='-', end='\n')

print('Red', 'Green', 'Blue', sep=',', end='@')
print('hehe')


# --- Content from seperator.py ---
a = 12
b = 12
c = 2022
print(a, b, c, sep="-")


# --- Content from seperator2.py ---
print(10, 20, sep=' - ', 30)


# --- Content from end parameter.py ---
# ends the output with a space
print("Welcome to", end=' ')
print("real world", end=' ')


# --- Content from end parameter2.py ---
# ends the output with '@'
print("lalala", end='@')
print("hehhehee")


# --- Content from end parameter3.py ---
name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.", end=" ")
print("Nice to meet you!")


# --- Content from escapesequence.py ---
# Python Program for
# Escape Sequencing
# of String

# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Python\nGeeks"
print("\nNew Line: ")
print(String1)


# --- Content from comment.py ---
# This is a comment
# Print “monkey. d. luffy” to console
print("monkey. d. luffy")


# --- Content from comment1.py ---
a, b = 1, 3  # Declaring two integers
sum = a + b  # adding two integers
print(sum)  # displaying the output


# --- Content from comment2.py ---
# This is a comment
# This is second comment
# Print “uzumaki” to console
print("uzumaki")


# --- Content from comment3.py ---
"""
This would be a multiline comment in Python that
spans several lines and describes dattebayo.
"""
print("dattebayo")


# --- Content from comment4.py ---
'''This article on haha gives you a
perfect example of
multi-line comments'''

print("haha")


# --- Content from docstring.py ---
def helloWorld():
    # This is a docstring comment
    """ This program prints out hello world """
    print("Hello World")


helloWorld()


# --- Content from identation.py ---
# Python indentation

site = 'baka'

if site == 'baka':
    print('Logging on to one piece')
else:
    print('retype the URL.')
print('All set !')


# --- Content from hellooctal.py ---
# Printing hello in octal
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1)

# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


# --- Content from true false none.py ---
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])
