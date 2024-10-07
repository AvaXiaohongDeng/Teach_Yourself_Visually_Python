# data_types.py

# 1. Integers
def integer_operations():
    print("Integers")
    integer_value = 10
    print("Integer:", integer_value)
    # Integer operations:
    print("Exponentiation:", integer_value ** 2)  # 10^2 = 100

# 2. Float (Floating-Point Numbers)
def float_operations():
    print("\nFloat (Floating-Point Numbers)")
    float_value = 3.14
    print("Float:", float_value)
    # Float operations:
    print("Float Division:", float_value / 2)
    print("Rounded Float:", round(float_value, 1))

# 3. Strings
def string_operations():
    print("\nStrings")
    string_value = "Hello Python"
    print("String:", string_value)
    # String operations:
    print("Uppercase:", string_value.upper())
    print("Replace:", string_value.replace("Python", "World"))
    print("Length of String:", len(string_value))

    # Find the index of the space character
    index_split = string_value.find(" ")
    
    # Get the first word of the string
    first_word = string_value[0:index_split]  # Use ':' for slicing
    print("First word of String:", first_word)

# 4. List
def list_operations():
    print("\nLists")
    list_value = [1, 2, 3, 4, 5]
    print("List:", list_value)
    # Common List operations:
    list_value.append(6)  # Add item to the list
    print("Appended List:", list_value)
    list_value.pop()  # Remove last item
    print("List after Pop:", list_value)
    print("Slice of List:", list_value[1:4])  # Get sublist

# 5. Tuple
def tuple_operations():
    print("\nTuples")
    tuple_value = (10, 20, 30)
    print("Tuple:", tuple_value)
    # Tuple operations:
    print("First element of Tuple:", tuple_value[0])
    print("Length of Tuple:", len(tuple_value))
    print("How many '10' in Tuple:", tuple_value.count(10))

# 6. Set
def set_operations():
    print("\nSets")
    set_value = {1, 2, 3, 4, 5}
    print("Set:", set_value)
    # Set operations:
    set_value.add(6)  # Add element
    print("Set after Adding:", set_value)
    set_value.remove(2)  # Remove element
    print("Set after Removing 2:", set_value)
    set_value = set_value.union({7, 8})
    print("Set after Union with {7, 8}:", set_value)

# 7. Dictionary
def dictionary_operations():
    print("\nDictionaries")
    dict_value = {"name": "Alice", "age": 25, "city": "Toronto"}
    print("Dictionary:", dict_value)
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
def boolean_operations():
    print("\nBooleans")
    bool_value = True
    print("Boolean:", bool_value)
    # Boolean operations:
    print("Not Operation:", not bool_value)
    print("Boolean AND:", bool_value and False)

# 9. NoneType
def none_operations():
    print("\nNoneType")
    none_value = None
    print("NoneType:", none_value)
    # NoneType operations:
    print("Check if None:", none_value is None)

# Function to check and demonstrate data types
def data_type_check():
    dict_value = {"name": "Alice", "age": 30}
    dict_type = type(dict_value)
    print(f"\ndict_value's type is {dict_type}.")

def input_conversion_example():
    print("\nInput and Conversion Example")
    input1 = input("Enter a float whose integer part is 1: ")
    try:
        float1 = float(input1)
        print("Float entered:", float1)
        
        # Convert float to integer
        integer1 = int(float1)
        print("Converted to integer:", integer1)
        
        # Convert integer to boolean
        boolean1 = bool(integer1)
        print("Converted to boolean:", boolean1)
    except ValueError:
        print("Invalid input! Please enter a valid float number.")

if __name__ == "__main__":
    integer_operations()
    float_operations()
    string_operations()
    list_operations()
    tuple_operations()
    set_operations()
    dictionary_operations()
    boolean_operations()
    none_operations()
    data_type_check()
    input_conversion_example()
