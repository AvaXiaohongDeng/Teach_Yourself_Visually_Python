# dictionary_operations.py

# A Python dictionary is an unordered, mutable, and indexed collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, or tuples), and values can be of any type.

# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

print("Initial Dictionary:", my_dict)

# ---------------------------
# Common Dictionary Operations
# ---------------------------

# Accessing a value using its key
print("\nAccessing value for 'name':", my_dict['name'])

# Adding or updating an entry
my_dict['age'] = 31  # Update existing key
my_dict['job'] = 'Engineer'  # Add new key-value pair
print("After Adding/Updating:", my_dict)

# Removing a key-value pair using pop()
removed_value = my_dict.pop('city')
print("\nAfter Removing 'city':", my_dict)
print("Removed Value:", removed_value)

# Removing the last inserted key-value pair using popitem()
key, value = my_dict.popitem()
print("\nAfter popitem():", my_dict)
print(f"Removed pair: ({key}: {value})")

# Checking if a key exists
if 'name' in my_dict:
    print("\nKey 'name' exists in the dictionary.")

# ---------------------------
# Dictionary Methods
# ---------------------------

# clear(): Removes all elements from the dictionary
my_dict.clear()
print("\nAfter clear():", my_dict)

# Resetting the dictionary
my_dict = {'name': 'Alice', 'age': 22, 'gender': 'Female'}

# copy(): Creates a shallow copy of the dictionary
dict_copy = my_dict.copy()
print("\nOriginal Dictionary:", my_dict)
print("Copied Dictionary:", dict_copy)

# fromkeys(): Creates a dictionary with specified keys and a default value
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)  # All keys will have value 0
print("\nDictionary from keys:", default_dict)

# get(): Returns the value of the specified key. If the key doesn't exist, it returns a default value (None or specified).
print("\nGet value for 'name':", my_dict.get('name'))
print("Get value for non-existent key 'city':", my_dict.get('city', 'Not Found'))

# items(): Returns a view object that contains key-value pairs as tuples
print("\nDictionary items:", my_dict.items())

# keys(): Returns a view object that contains the keys of the dictionary
print("Dictionary keys:", my_dict.keys())

# values(): Returns a view object that contains the values of the dictionary
print("Dictionary values:", my_dict.values())

# setdefault(): Returns the value of the specified key. If the key doesn't exist, it inserts the key with the specified value.
my_dict.setdefault('job', 'Student')
print("\nAfter setdefault('job', 'Student'):", my_dict)

# update(): Updates the dictionary with elements from another dictionary or iterable of key-value pairs
new_info = {'age': 23, 'city': 'Toronto'}
my_dict.update(new_info)
print("\nAfter update():", my_dict)

# pop(): Removes a specific key-value pair and returns its value
removed_age = my_dict.pop('age')
print("\nAfter pop('age'):", my_dict)
print("Removed age:", removed_age)

# ---------------------------
# Dictionary Comprehensions
# ---------------------------
# Creating a dictionary from two lists using dictionary comprehension
keys = ['name', 'age', 'city']
values = ['Alice', 23, 'Toronto']
combined_dict = {keys[i]: values[i] for i in range(len(keys))}
print("\nDictionary Comprehension:", combined_dict)

# ---------------------------
# Looping Through a Dictionary
# ---------------------------
print("\nLooping through keys:")
for key in my_dict:
    print(key)

print("\nLooping through values:")
for value in my_dict.values():
    print(value)

print("\nLooping through key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# ---------------------------
# Nested Dictionary
# ---------------------------
# A dictionary can contain other dictionaries
nested_dict = {
    'student1': {'name': 'Bob', 'age': 20},
    'student2': {'name': 'Charlie', 'age': 21},
}

print("\nNested Dictionary:", nested_dict)
print("Accessing Nested Dictionary:", nested_dict['student1']['name'])

