# decision_making_statements.py

# 1. if-elif-else statement
def check_temperature(temp):
    if temp > 30:
        print("It's a hot day.")
    elif temp >= 20:
        print("It's a nice day.")
    else:
        print("It's a cold day.")

print("1. if-elif-else example:")
temperature = 25
check_temperature(temperature)  # This will call the function with the temperature variable

# 2. while statement
def count_down(n):
    print("\n2. while loop example:")
    while n > 0:
        print(n)
        n -= 1
    else:
        print("Liftoff!")

count_down(5)  # This will count down from 5 to 1 and then print "Liftoff!"

# 3. try-except statement
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"\n3. try-except example: Division result: {result}")
    except ZeroDivisionError:
        print("\nCannot divide by zero!")
    finally:
        print("This block always executes.")

divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero error will be caught

# 4. for statement (iteration over a list)
def print_even_numbers(numbers):
    print("\n4. for loop example: Even numbers in the list")
    for number in numbers:
        if number % 2 == 0:
            print(number)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers_list)  # This will print only the even numbers from the list

# 5. Nested loops example
def nested_loops_example():
    print("\n5. Nested loops example:")
    for i in range(1, 4):  # Outer loop
        for j in range(1, 4):  # Inner loop
            print(f"i = {i}, j = {j}")

nested_loops_example()  # This will demonstrate a simple nested loop

# 6. Dictionaries to map cases to specific functions (alternative to switch-case)
def case_1():
    return "You chose case 1."

def case_2():
    return "You chose case 2."

def default_case():
    return "Invalid choice."

def handle_choice(choice):
    switch = {
        1: case_1,
        2: case_2
    }
    # Get the function from the dictionary or use default_case if choice is not found
    return switch.get(choice, default_case)()

print("\n6. Dictionary to map cases example:")
user_choice = 2
print(f"User selected: {user_choice}")
print(handle_choice(user_choice))  # Calls the case_2 function

user_choice = 5
print(f"User selected: {user_choice}")
print(handle_choice(user_choice))  # Calls the default_case function
