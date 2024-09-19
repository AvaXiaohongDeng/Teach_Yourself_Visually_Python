#file_operations.py

import os       # Provides methods for working with the file system.
import shutil   # Provides methods for file and directory operations.

# Open a file for writing (creates if not exists, truncates if exists)
print("\n1. Open a file for writing ('w'):")
# Explanation: Create the file if it does not exist; delete its contents if it does exist. Open the file in write mode with the pointer at the beginning.
try:
    with open('example_w.txt', 'w') as file:
        file.write("This file is opened in write mode.")
        print("File 'example_w.txt' opened for writing and data written.")
except IOError as e:
    print("Error opening file for writing:", e)

# Open a file for reading (file must exist), the pointer is at the beginning.
print("\n2. Open a file for reading ('r'):")
# Explanation: Open the file in read mode with the pointer at the beginning. If the file does not exist, an error occurs.
try:
    with open('example_w.txt', 'r') as file:
        content = file.read()
        print("Content of 'example_w.txt':", content)
except IOError as e:
    print("Error opening file for reading:", e)

# Open a file for appending (creates if not exists), the pointer is at the end.
print("\n3. Open a file for appending ('a'):")
# Explanation: Create the file if it does not exist. Open the file in append mode with the pointer at the end.
try:
    with open('example_w.txt', 'a') as file:
        file.write("\nAppending more data.")
        print("Data appended to 'example_w.txt'.")
except IOError as e:
    print("Error opening file for appending:", e)

# Open a file exclusively for creation ('x')
print("\n4. Open a file exclusively for creation ('x'):")
# Explanation: Create the specified file and then open it with the pointer at the beginning. If the file already exists, an error occurs.
try:
    with open('example_x.txt', 'x') as file:
        file.write("This file is created using exclusive creation mode.")
        print("File 'example_x.txt' created with exclusive mode.")
except FileExistsError:
    print("File 'example_x.txt' already exists. Could not create file.")
except IOError as e:
    print("Error opening file for exclusive creation:", e)
    
# Open a file for both reading and writing (creates if not exists)
print("\n5. Open a file for reading and writing ('r+'):")
# Explanation: Open the file in read and write mode with the pointer at the beginning. If the file does not exist, an error occurs.
try:
    with open('example_w.txt', 'r+') as file:
        file.write("\nUpdating data.")
        file.seek(0, os.SEEK_SET)  # Move to the beginning of the file
        content = file.read()
        print("Updated content of 'example_w.txt':", content)
except IOError as e:
    print("Error opening file for reading and writing:", e)

# Open a file for reading and writing (create if not exists)
print("\n6. Open a file for reading and writing ('w+'):")
# Explanation: Create the file if it does not exist; delete its contents if it does exist. Open the file in write and read mode with the pointer at the beginning.
try:
    with open('example_w_plus.txt', 'w+') as file:
        file.write("This is a new file with 'w+' mode.")
        file.seek(0, os.SEEK_SET)  # Move to the beginning of the file
        content = file.read()
        print("Content of 'example_w_plus.txt':", content)
except IOError as e:
    print("Error opening file for reading and writing:", e)

# Open a file for appending and reading ('a+')
print("\n7. Open a file for appending and reading ('a+'):")
# Explanation: Create the file if it does not exist. Open the file in append and read mode with the pointer at the end.
try:
    with open('example_w_plus.txt', 'a+') as file:
        file.write("\nAppending some more data.")
        file.seek(0)  # Move to the beginning of the file
        content = file.read()
        print("Content of 'example_w_plus.txt' after appending:", content)
except IOError as e:
    print("Error opening file for appending and reading:", e)

# Check if a file is open
print("\n8. Check if a file is open:")
file = open('example_w_plus.txt', 'r')
try:
    print("File name: ", file.name)
    print("File 'example_w_plus.txt' is open:", not file.closed)
finally:
    file.close()
    print("File 'example_w_plus.txt' closed:", file.closed)

# Closing files
print("\n9. Ways to close files:")
file = open('example_w.txt', 'r')
file.close()  # Explicitly closing the file
print("File 'example_w.txt' closed:", file.closed)

# Using `with` automatically handles closing
print("\nFile closed automatically using 'with' context manager.")
