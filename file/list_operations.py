# list_operations.py

# 1. What is a List?
# A list in Python is a mutable, ordered collection of elements. Lists can store items of different types, including integers, strings, and even other lists.

# Example of creating a list:
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# 2. Accessing List Elements:
# Lists are indexed starting from 0, meaning the first element has index 0.

# Accessing elements by index:
print("\nFirst element (my_list[0]):", my_list[0])
print("Last element (my_list[-1]):", my_list[-1])  # Negative indexing starts from the end

# 3. Modifying List Elements:
# Lists are mutable, so you can modify elements directly.
my_list[0] = 100  # Modifying the first element
print("\nModified List:", my_list)

# 4. Common List Methods:

# (a) append(): Adds an element to the end of the list.
my_list.append(60)
print("\nList after append(60):", my_list)

# (b) insert(): Inserts an element at a specific index.
my_list.insert(1, 15)  # Inserts 15 at index 1
print("List after insert(1, 15):", my_list)

# (c) extend(): Adds elements from another list (or any iterable) to the end of the list.
another_list = [70, 80]
my_list.extend(another_list)
print("List after extend([70, 80]):", my_list)

# (d) pop(): Removes and returns the element at the given index (default is the last element).
removed_element = my_list.pop()  # Removes the last element
print("\nRemoved element using pop():", removed_element)
print("List after pop():", my_list)

# You can also pop a specific index:
removed_element = my_list.pop(2)  # Removes element at index 2
print("Removed element at index 2 using pop(2):", removed_element)
print("List after pop(2):", my_list)

# (e) remove(): Removes the first occurrence of a specific element.
my_list.remove(15)  # Removes the first occurrence of 15
print("\nList after remove(15):", my_list)

# (f) sort(): Sorts the list in ascending order (modifies the list in place).
my_list.sort()
print("List after sort():", my_list)

# You can also sort in descending order using reverse=True.
my_list.sort(reverse=True)
print("List after sort(reverse=True):", my_list)

# (g) reverse(): Reverses the order of the list (modifies the list in place).
my_list.reverse()
print("\nList after reverse():", my_list)

# (h) index(): Returns the index of the first occurrence of an element.
index_of_100 = my_list.index(100)
print("\nIndex of 100 in my_list:", index_of_100)

# (i) count(): Returns the number of occurrences of a specific element.
count_of_100 = my_list.count(100)
print("Count of 100 in my_list:", count_of_100)

# (j) clear(): Removes all elements from the list.
my_list.clear()
print("\nList after clear():", my_list)

# 5. Copying Lists:

# Shallow copy using copy() method:
list_copy = another_list.copy()
print("\nOriginal another_list:", another_list)
print("Copied list:", list_copy)

# Modifying the copied list doesn't affect the original list:
list_copy.append(90)
print("Modified copied list:", list_copy)
print("Original another_list remains unchanged:", another_list)

# 6. List Comprehension:
# List comprehension is a concise way to create lists based on existing lists.

# Example: Creating a list of squares from 0 to 4
squares = [x ** 2 for x in range(5)]
print("\nList comprehension (squares of 0 to 4):", squares)

# 7. Other Useful List Functions:

# (a) len(): Returns the number of elements in the list.
length_of_list = len(another_list)
print("\nLength of another_list:", length_of_list)

# (b) sum(): Returns the sum of elements in the list (works with numerical lists).
sum_of_list = sum(another_list)
print("Sum of another_list:", sum_of_list)

# (c) min() and max(): Returns the smallest and largest elements in the list.
min_value = min(another_list)
max_value = max(another_list)
print("Minimum value in another_list:", min_value)
print("Maximum value in another_list:", max_value)

# 8. Nested Lists (Lists within lists):
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested List:", nested_list)

# Accessing elements in nested lists:
first_sublist = nested_list[0]  # Access the first list [1, 2, 3]
print("First sublist:", first_sublist)

first_element_in_first_sublist = nested_list[0][0]  # Access the first element of the first list (1)
print("First element in first sublist:", first_element_in_first_sublist)

# 9. Slicing Lists:
# Slicing allows you to access a part of the list by specifying a start and end index.

# Example of slicing:
sliced_list = my_list[1:4]  # Gets elements from index 1 to 3 (4 is not included)
print("\nSliced List (my_list[1:4]):", sliced_list)

# You can also use negative indices for slicing:
sliced_list_negative = my_list[-3:]  # Gets the last 3 elements
print("Sliced List (my_list[-3:]):", sliced_list_negative)

# You can also specify a step:
sliced_list_step = my_list[::2]  # Gets every second element
print("Sliced List (my_list[::2]):", sliced_list_step)

# Reversing a list:
list1 = [1, 2, 3]
list2 = list1[::-1]  # Using slicing to reverse the list
print("\nReversed list using slicing:", list2)

# Conclusion:
# Lists in Python are versatile and powerful. With various methods like append(), pop(), and sort(), they allow flexible data handling.
