# --- Content from list_examples.py ---
list

# creates a empty list
nums = []

# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)


# --- Content from list1.py ---
# Declaring a list
L = [1, "a", "string", 1 + 2]
print
L
# Adding an element in the list
L.append(6)
print
L
# Deleting last element from a list
L.pop()
print
L
# Displaying Second element of the list
print
L[1]


# --- Content from list2.py ---
Var = ["Geeks", "for", "Geeks"]
print(Var)


# --- Content from listsize.py ---
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))


# --- Content from iteration_list.py ---
L = [1, 4, 5, 7, 8, 9]
for i in L:
    print(i)


# --- Content from listaccess.py ---
# Python program to demonstrate
# accessing of element from list

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])


# --- Content from listaccess2.py ---
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [["Geeks", "For"], ["Geeks"]]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])


# --- Content from listadd3.py ---
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, "Geeks", "Always"])
print("\nList after performing Extend Operation: ")
print(List)


# --- Content from listaddition.py ---
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ["For", "Geeks"]
List.append(List2)
print("\nList after Addition of a List: ")
print(List)


# --- Content from listaddition2.py ---
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, "Geeks")
print("\nList after performing Insert Operation: ")
print(List)


# --- Content from listcreation.py ---
# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])


# --- Content from listcreation2.py ---
# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, "Geeks", 4, "For", 6, "Geeks"]
print("\nList with the use of Mixed Values: ")
print(List)


# --- Content from listindex.py ---
List = [1, 2, "Geeks", 4, "For", 6, "Geeks"]

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])


# --- Content from listinput.py ---
# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()
print("The list is:", lst)  # printing the list


# --- Content from listinput2.py ---
# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(
    map(
        int,
        input(
            "Enter the integer\
elements:"
        )
        .strip()
        .split(),
    )
)[:n]

# printing the list
print("The list is:", lst)


# --- Content from listremove.py ---
# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)


# --- Content from listremove2.py ---
# Creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)


# --- Content from listreverse.py ---
# Reversing a list
mylist = [1, 2, 3, 4, 5, "Geek", "Python"]
mylist.reverse()
print(mylist)
