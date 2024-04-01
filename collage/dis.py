# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs to the dictionary
my_dict['apple'] = 10
my_dict['banana'] = 5
my_dict['orange'] = 8

# Printing the dictionary
print("Original Dictionary:", my_dict)

# Accessing value by key
print("Value of 'apple':", my_dict['apple'])

# Modifying value by key
my_dict['banana'] = 7
print("Modified Dictionary:", my_dict)

# Removing a key-value pair
del my_dict['orange']
print("Dictionary after removing 'orange':", my_dict)

# Checking if a key exists in the dictionary
key = 'apple'
if key in my_dict:
    print(f"'{key}' exists in the dictionary with a value of {my_dict[key]}")
else:
    print(f"'{key}' does not exist in the dictionary")

# Iterating through key-value pairs in the dictionary
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Getting the number of key-value pairs in the dictionary
print("Number of items in the dictionary:", len(my_dict))

# Clearing the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)
