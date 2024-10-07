# error_handling.py

# 1. Common Python Errors:
# Python errors (exceptions) occur during execution and can stop a program unless handled.
# Below are some common Python error types:

# a) SyntaxError: Occurs when the code is not properly structured (invalid Python syntax).
# Example:
#   print("Hello)  # SyntaxError (missing closing quote)

# b) NameError: Occurs when trying to access a variable that has not been defined.
# Example:
#   print(x)  # NameError: 'x' is not defined

# c) TypeError: Happens when an operation is applied to an object of an inappropriate type.
# Example:
#   result = "10" + 5  # TypeError: cannot concatenate str and int

# d) ValueError: Raised when a function gets an argument of the correct type but inappropriate value.
# Example:
#   number = int("abc")  # ValueError: invalid literal for int()

# e) IndexError: Occurs when trying to access an index that is out of range in a list or string.
# Example:
#   my_list = [1, 2, 3]
#   print(my_list[5])  # IndexError: list index out of range

# f) KeyError: Raised when trying to access a non-existent key in a dictionary.
# Example:
#   my_dict = {"name": "Alice"}
#   print(my_dict["age"])  # KeyError: 'age'

# 2. Handling Errors with try...except
# You can handle errors using a try-except block to catch exceptions and prevent the program from crashing.

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# The above block "catches" the exception and prints a custom message instead of stopping the program.

# You can also catch multiple exceptions:
try:
    number = int("abc")  # ValueError
    result = 10 / 0  # ZeroDivisionError
except ValueError:
    print("A ValueError occurred.")
except ZeroDivisionError:
    print("A ZeroDivisionError occurred.")

# Catching all exceptions (not recommended for debugging but useful for logging):
try:
    print(10 / 0)
except Exception as e:
    print(f"An error occurred: {e}")

# 3. Using `else` and `finally` with try...except
# - `else`: The block that runs if no exceptions were raised in the try block.
# - `finally`: The block that runs regardless of whether an exception was raised or not, often used for cleanup.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful: {result}")
finally:
    print("This runs no matter what.")

# 4. Raising Exceptions
# You can manually raise exceptions in Python using the `raise` statement.

# Example: Raise a ValueError if an invalid input is provided.
def check_positive_number(number):
    if number < 0:
        raise ValueError("Number must be positive!")
    return number

try:
    check_positive_number(-5)
except ValueError as ve:
    print(f"Error: {ve}")

# 5. Custom Exceptions
# You can define your own exception classes in Python by inheriting from the base `Exception` class.

class CustomError(Exception):
    """Custom Exception for specific errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example: Raising the custom exception
def check_even_number(number):
    if number % 2 != 0:
        raise CustomError(f"{number} is not an even number!")
    return number

try:
    check_even_number(5)
except CustomError as ce:
    print(f"Custom error occurred: {ce}")

# 6. Common built-in exception methods

# - `assert` statement: Used to assert a condition is true, otherwise raises an AssertionError.
def divide(a, b):
    assert b != 0, "b cannot be zero!"
    return a / b

try:
    divide(10, 0)  # Will trigger AssertionError
except AssertionError as ae:
    print(f"Assertion error: {ae}")

# - `logging` module: For handling errors in production code and debugging.
import logging

logging.basicConfig(level=logging.ERROR)

def log_error_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        return None

result = log_error_divide(10, 0)  # Logs the error but doesn't stop execution

# 7. Conclusion
# Python offers various ways to handle exceptions using try-except blocks, raising exceptions manually, and creating custom exceptions.
# Proper error handling improves code robustness and user experience.
