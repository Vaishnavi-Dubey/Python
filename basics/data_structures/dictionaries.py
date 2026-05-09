# --- Content from dictionary.py ---
# Dictionary

# creates a empty list
Dict = []

# putting integer values
Dict = {1: "Geeks", 2: "For", 3: "Geeks"}

print(Dict)


# --- Content from dictionary2.py ---
# Create a new dictionary
d = dict()  # or d = {}

# Add a key - value pairs to dictionary
d["xyz"] = 123
d["abc"] = 345

# print the whole dictionary
print(d)

# print only the keys
print(d.keys())

# print only values
print(d.values())

# iterate over dictionary
for i in d:
    print("%s %d" % (i, d[i]))

# another method of iteration
for index, key in enumerate(d):
    print(index, key, d[key])

# check if key exist
print("xyz" in d)

# delete the key-value pair
del d["xyz"]

# check again
print("xyz" in d)
