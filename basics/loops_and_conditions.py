

# --- Content from if else elif.py ---
i = 20
if (i == 10):
    print("i is 10")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")


# --- Content from for loop.py ---
for step in range(5):
    print(step)


# --- Content from for while break continue.py ---
# Using for loop
for i in range(10):

    print(i, end=" ")

    # break the loop as soon it sees 6
    if i == 6:
        break

print()

# loop from 1 to 10
i = 0
while i < 10:

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")

    i += 1


# --- Content from pass_examples.py ---
n = 10
for i in range(n):
    # pass can be used as placeholder
    # when code is to added later
    pass


# --- Content from selectionSatement.py ---
num1 = 34
if (num1 > 12):
    print("Num1 is good")
elif (num1 > 35):
    print("Num2 is not gooooo....")
else:
print("Num2 is great")


# --- Content from iteration_range.py ---
for i in range(0, 10):
	print(i)


# --- Content from iterations.py ---
i = 1
while (i < 10):
    print(i)
    i += 1
