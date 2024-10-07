# operators.py

# Arithmetic Operators
def arithmetic_operators(a, b):
    # Implements mathematical operations in the standard order given by the acronym PEMDAS
    # PEMDAS: Parentheses, Exponentiation, Multiplication, Division, Addition, Subtraction
    print("Arithmetic Operators")
    print(f"{a} + {b} = {a + b}")  # Addition
    print(f"{a} - {b} = {a - b}")  # Subtraction
    print(f"{a} * {b} = {a * b}")  # Multiplication
    print(f"{a} / {b} = {a / b}")  # Division
    print(f"{a} % {b} = {a % b}")  # Modulus
    print(f"{a} ** {b} = {a ** b}") # Exponentiation
    print(f"{a} // {b} = {a // b}") # Floor Division

# Assignment Operators
def assignment_operators():
    print("\nAssignment Operators")
    a = 5
    print(f"a = {a}")
    a += 3
    print(f"a += 3 -> {a}")
    a -= 2
    print(f"a -= 2 -> {a}")
    a *= 2
    print(f"a *= 2 -> {a}")
    a /= 2
    print(f"a /= 2 -> {a}")
    a %= 3
    print(f"a %= 3 -> {a}")
    a **= 2
    print(f"a **= 2 -> {a}")
    a //= 3
    print(f"a //= 3 -> {a}")

# Comparison Operators
def comparison_operators(a, b):
    print("\nComparison Operators")
    print(f"{a} == {b} -> {a == b}") # Equal
    print(f"{a} != {b} -> {a != b}") # Not equal
    print(f"{a} > {b} -> {a > b}")   # Greater than
    print(f"{a} < {b} -> {a < b}")   # Less than
    print(f"{a} >= {b} -> {a >= b}") # Greater than or equal to
    print(f"{a} <= {b} -> {a <= b}") # Less than or equal to

# Logical Operators
def logical_operators(a, b):
    print("\nLogical Operators")
    print(f"{a} and {b} -> {a and b}") # Logical AND
    print(f"{a} or {b} -> {a or b}")   # Logical OR
    print(f"not {a} -> {not a}")       # Logical NOT

# Identity Operators
def identity_operators(a, b):
    print("\nIdentity Operators")
    print(f"{a} is {b} -> {a is b}")   # Is operator
    print(f"{a} is not {b} -> {a is not b}") # Is not operator

# Membership Operators
def membership_operators(element, container):
    print("\nMembership Operators")
    print(f"{element} in {container} -> {element in container}")     # In operator
    print(f"{element} not in {container} -> {element not in container}") # Not in operator

# Bitwise Operators
def bitwise_operators(a, b):
    print("\nBitwise Operators")
    print(f"{a} & {b} -> {a & b}")   # AND
    print(f"{a} | {b} -> {a | b}")   # OR
    print(f"{a} ^ {b} -> {a ^ b}")   # XOR
    print(f"~{a} -> {~a}")           # NOT
    print(f"{a} << 2 -> {a << 2}")   # Left shift
    print(f"{a} >> 2 -> {a >> 2}")   # Right shift

if __name__ == "__main__": 
    a = 10
    b = 5
    arithmetic_operators(a, b)
    assignment_operators()
    comparison_operators(a, b)
    logical_operators(True, False)
    identity_operators(a, b)
    membership_operators(3, [1, 2, 3, 4, 5])
    bitwise_operators(a, b)
