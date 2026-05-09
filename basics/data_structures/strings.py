# --- Content from string_examples.py ---
# Assigning string to a variable
a = "This is a string"
print(a)
b = "This is a string"
print(b)
c = """This is a string"""
print(c)


# --- Content from string2.py ---
# Creation of String

# Creating a String with single Quotes
String1 = "Welcome to the World"
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String with double Quotes
String1 = "I'm"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String with triple Quotes
String1 = """I'm a smart and I live in a world"""
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple Quotes allows multiple lines
String1 = """weebs
			For
			Life"""
print("\nCreating a multiline String: ")
print(String1)


# --- Content from string3.py ---
# Access characters of String

String1 = "hehehehehe"
print("Initial String: ")
print(String1)

# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])


# --- Content from string4.py ---
# Program to reverse a string
gfg = "shhhhhh"
print(gfg[::-1])


# --- Content from stringUpdate2.py ---
# Update entire String

String1 = "Hello, how're you?"
print("Initial String: ")
print(String1)

# Updating a String
String1 = "Welcome to the World"
print("\nUpdated String: ")
print(String1)


# --- Content from stringalignment.py ---
# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format("Geeks", "for", "Geeks")
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)


# --- Content from stringchardelete.py ---
# Delete characters from a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character
# of the String
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)


# --- Content from stringdelete.py ---
# Python Program to Delete
# entire String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a String
# with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)


# --- Content from stringformat.py ---
# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format("Geeks", "For", "Life")
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format("Geeks", "For", "Life")
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g="Geeks", f="For", l="Life")
print("\nPrint String in order of Keywords: ")
print(String1)


# --- Content from stringformat2.py ---
# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(1 / 6)
print("\none-sixth is : ")
print(String1)


# --- Content from stringformat3.py ---
# Python Program for
# Old Style Formatting
# of Integers

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print("The value of Integer1 is %3.2f" % Integer1)
print("\nFormatting in 3.4f format: ")
print("The value of Integer1 is %3.4f" % Integer1)


# --- Content from stringreverse.py ---
# Program to reverse a string

gfg = "shhhhhhhhh"

# Reverse the string using reversed and join function
gfg = "".join(reversed(gfg))

print(gfg)


# --- Content from stringslicing.py ---
# Creating a String
String1 = "hehehehehe"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String1[3:-2])


# --- Content from stringupdate.py ---
# Update character of a String

String1 = "Hello, how are you?"
print("Initial String: ")
print(String1)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
# there are following two ways
# 1
list1 = list(String1)
list1[2] = "p"
String2 = "".join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

# 2
String3 = String1[0:2] + "p" + String1[3:]
print(String3)


# --- Content from iteration_string.py ---
s = "Hello World"
for i in s:
    print(i)
