# Introduction to Python Data Types

# 1. Integers
# Integers are whole numbers without a fractional part.
# Example: 5, -10, 100
integer_value = 10
print("Integer:", integer_value)
# Integer operations:
print("Exponentiation:", integer_value ** 2)  # 10^2 = 100

# 2. Float (Floating-Point Numbers)
# Floats are numbers with a decimal point.
# Example: 3.14, -2.5, 0.001
float_value = 3.14
print("\nFloat:", float_value)
# Float operations:
print("Float Division:", float_value / 2)
print("Rounded Float:", round(float_value, 1))

# 3. Strings
# Strings are sequences of characters enclosed in quotes.
# Example: "Hello, World!", 'Python'
string_value = "Hello Python"
print("\nString:", string_value)
# String operations:
print("Uppercase:", string_value.upper())
print("Replace:", string_value.replace("Python", "World"))
print("Length of String:", len(string_value))

# Find the index of the space character
indexSplit = string_value.find(" ")

# Get the first word of the string
firstWord = string_value[0:indexSplit]  # Use ':' for slicing, not ','
print("First word of String:", firstWord)

# 4. List
# Lists are ordered, mutable (changeable) collections of items.
# Example: [1, 2, 3], ["apple", "banana", "cherry"]
list_value = [1, 2, 3, 4, 5]
print("\nList:", list_value)
# Common List operations:
list_value.append(6)  # Add item to the list
print("Appended List:", list_value)
list_value.pop()  # Remove last item
print("List after Pop:", list_value)
print("Slice of List:", list_value[1:4])  # Get sublist

# 5. Tuple
# Tuples are ordered, immutable (unchangeable) collections of items.
# Example: (1, 2, 3), ("red", "green", "blue")
tuple_value = (10, 20, 30)
print("\nTuple:", tuple_value)
# Tuple operations:
print("First element of Tuple:", tuple_value[0])
print("Length of Tuple:", len(tuple_value))
print("How many '10' in Tuple:", tuple_value.count(10))

# 6. Set
# Sets are unordered collections of unique items.
# Example: {1, 2, 3}, {"apple", "banana", "cherry"}
set_value = {1, 2, 3, 4, 5}
print("\nSet:", set_value)
# Set operations:
set_value.add(6)  # Add element
print("Set after Adding:", set_value)
set_value.remove(2)  # Remove element
print("Set after Removing 2:", set_value)
set_value = set_value.union({7, 8})
print("Set after Union with {7, 8}:", set_value)

# 7. Dictionary
# Dictionaries are unordered collections of key-value pairs.
# Example: {"name": "Alice", "age": 25}
dict_value = {"name": "Alice", "age": 25, "city": "Toronto"}
print("\nDictionary:", dict_value)

# Dictionary operations:
print("Get 'name':", dict_value.get("name"))
dict_value["age"] = 30  # Update value
print("Updated Dictionary:", dict_value)
del dict_value["city"]  # Remove a key-value pair
print("Dictionary after Deletion:", dict_value)

# Loop through dictionary and print key-value pairs
for item in dict_value:
    print(f"{item}: {dict_value[item]}")

# 8. Boolean
# Booleans represent True or False values.
# Example: True, False
# Return False: the value False; the value None; the number zero or 0; an empty string/list/tuple/dictionary
bool_value = True
print("\nBoolean:", bool_value)
# Boolean operations:
print("Not Operation:", not bool_value)
print("Boolean AND:", bool_value and False)

# 9. NoneType
# None represents the absence of a value or a null value.
# Example: None
none_value = None
print("\nNoneType:", none_value)
# None doesn't support many operations, but it is often used as a placeholder or default value in functions.
print("Check if None:", none_value is None)

# Data type check function
dict_type = type(dict_value)
print(f"dict_value's type is {dict_type}.")

# Input, data conversion, and boolean example
# Basic input validation to ensure correct input type
input1 = input("Enter a float whose integer part is 1: ")
try:
    float1 = float(input1)
    print("Float entered:", float1)
    
    # Convert float to integer
    integer1 = int(float1)
    print("Converted to integer:", integer1)
    
    # Convert integer to boolean
    # bool(0) will return False, any non-zero integer will return True
    boolean1 = bool(integer1)
    print("Converted to boolean:", boolean1)

except ValueError:
    print("Invalid input! Please enter a valid float number.")
