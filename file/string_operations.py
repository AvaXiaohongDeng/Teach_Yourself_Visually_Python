# string_operations.py

# 1. String Type in Python:
# In Python, a string is a sequence of characters enclosed within single ('') or double ("") quotes.
# Strings are immutable, meaning their contents cannot be changed after creation.

# Example of creating strings:
string1 = 'Hello, World!'  # Using single quotes
string2 = "Python is fun!"  # Using double quotes
multi_line_string = '''This is a
multi-line string'''  # Using triple quotes for multi-line strings

print("String 1:", string1)
print("String 2:", string2)
print("Multi-line String:", multi_line_string)

# 2. String Operations:

# Concatenation: Joining two or more strings using the + operator
concat_string = string1 + " " + string2
print("\nConcatenated String:", concat_string)

# Repetition: Repeat the string using the * operator
repeated_string = string1 * 2
print("Repeated String:", repeated_string)

# Indexing: Accessing characters in a string using their index (starts at 0)
first_char = string1[0]  # First character
last_char = string1[-1]  # Last character (negative indexing)

print("\nFirst character of string1:", first_char)
print("Last character of string1:", last_char)

# Slicing: Extracting a substring using slice notation [start:end:step]
substring = string1[0:5]  # Extracts 'Hello'
print("Sliced substring (0:5):", substring)

# 3. String Functions:

# len(): Returns the length of the string
length = len(string1)
print("\nLength of string1:", length)

# upper() and lower(): Converts the string to uppercase and lowercase
upper_string = string1.upper()
lower_string = string2.lower()
print("Uppercase string1:", upper_string)
print("Lowercase string2:", lower_string)

# strip(): Removes leading and trailing whitespace
string_with_spaces = "   Hello, World!   "
stripped_string = string_with_spaces.strip()
print("\nString with spaces:", string_with_spaces)
print("String after strip():", stripped_string)

# replace(): Replaces a substring with another substring
replaced_string = string1.replace("World", "Python")
print("Replaced String (World -> Python):", replaced_string)

# split(): Splits a string into a list of substrings based on a delimiter
split_string = string1.split(",")
print("Split string1 by ',' :", split_string)

# join(): Joins elements of a list into a single string using a delimiter
joined_string = " ".join(split_string)
print("Joined string:", joined_string)

# find(): Returns the index of the first occurrence of a substring
index_of_world = string1.find("World")
print("\nIndex of 'World' in string1:", index_of_world)

# isdigit(): Checks if the string consists of digits only
digit_string = "12345"
non_digit_string = "123abc"
print("\nIs digit_string all digits?", digit_string.isdigit())
print("Is non_digit_string all digits?", non_digit_string.isdigit())

# 4. Immutability of Strings
# Strings in Python cannot be modified after creation. To "modify" a string, we must create a new one.
immutable_string = "Hello"
new_string = immutable_string.replace("H", "J")  # Creates a new string

print("\nOriginal string:", immutable_string)
print("Modified (new) string:", new_string)

# 5. String Formatting

# (a) Using .format() method
formatted_string = "My name is {} and I am {} years old.".format("Alice", 30)
print("\nFormatted String using .format():", formatted_string)

# (b) Using % operator (interpolation operator)
# The `%` operator can be used for string interpolation similar to C-style formatting.
name = "Bob"
age = 25
interpolated_string = "My name is %s and I am %d years old." % (name, age)
print("Formatted String using % operator:", interpolated_string)

# (c) f-strings (formatted string literals)
# Introduced in Python 3.6+, f-strings make it easy to format strings.
f_string = f"My name is {name} and I am {age} years old."
print("Formatted String using f-string:", f_string)

# (d) Template strings (from the `string` module)
# Template strings are a safer option for user input and more advanced formatting
from string import Template
template = Template("My name is $name and I am $age years old.")
template_string = template.substitute(name="Charlie", age=28)
print("Formatted String using Template:", template_string)

# 6. String Transformation and Cleanup

# capitalize(): Capitalizes the first character of the string
capitalized_string = string2.capitalize()
print("\nCapitalized string2:", capitalized_string)

# title(): Capitalizes the first character of every word
title_string = "this is a title".title()
print("Title-cased string:", title_string)

# swapcase(): Swaps case – lower becomes upper and upper becomes lower
swapcase_string = string1.swapcase()
print("Swapcase string1:", swapcase_string)

# lstrip() and rstrip(): Removes leading and trailing spaces (left and right, respectively)
lstrip_string = string_with_spaces.lstrip()  # Removes leading spaces
rstrip_string = string_with_spaces.rstrip()  # Removes trailing spaces
print("\nString after lstrip():", lstrip_string)
print("String after rstrip():", rstrip_string)

# zfill(): Pads a string with zeros on the left, useful for formatting numbers
number_string = "42"
padded_number_string = number_string.zfill(5)
print("\nNumber string padded with zeros (zfill):", padded_number_string)

# casefold(): Similar to lower() but more aggressive for caseless matching, useful in comparisons
casefolded_string = "ß".casefold()  # 'ß' is a German character that becomes 'ss' with casefold
print("Casefolded string 'ß':", casefolded_string)

# 7. Cleaning Up Strings (Advanced)
# Using these methods, we can clean and format messy strings.

messy_string = "  HeLLo, WoRLd!  "
# Clean up by stripping, lowering, and replacing characters
cleaned_string = messy_string.strip().lower().replace("world", "everyone")
print("\nMessy string:", messy_string)
print("Cleaned-up string:", cleaned_string)
