# class_operations.py

# ----------------------------
# Python Classes and Objects
# ----------------------------

# A Python class is a blueprint for creating objects (instances).
# It can have attributes (variables) and methods (functions) that define its behavior.

# Defining a class
class Person:
    # The __init__ method is a special method that initializes the object's attributes.
    # It is called when a new instance of the class is created.
    def __init__(self, name, age):
        self.name = name  # Instance variable (attribute)
        self.age = age    # Instance variable (attribute)

    # Instance method (common method)
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance (object) of the class
person1 = Person('Alice', 25)
print("Person1 Type:", type(person1))

# Accessing attributes and calling methods
print("Person1 Name:", person1.name)  # Accessing attribute
person1.greet()  # Calling method

# ----------------------------
# Class Attributes and Methods
# ----------------------------

# Class attributes are shared among all instances of a class, unlike instance attributes.

class Car:
    wheels = 4  # Class attribute, shared by all instances

    def __init__(self, model, color):
        self.model = model  # Instance attribute
        self.color = color  # Instance attribute

    # Instance method
    def display_info(self):
        print(f"{self.model} is {self.color} and has {Car.wheels} wheels.")

# Creating two objects of the Car class
car1 = Car('Tesla', 'red')
car2 = Car('BMW', 'blue')

# Accessing the class attribute and instance method
car1.display_info()
car2.display_info()

# ----------------------------
# Types of Methods in a Class
# ----------------------------

class Calculator:

    # Class Method: A method that works on the class itself rather than an instance. Use @classmethod decorator.
    @classmethod
    def add(cls, a, b):
        return a + b

    # Static Method: A method that does not depend on class or instance variables. Use @staticmethod decorator.
    @staticmethod
    def subtract(a, b):
        return a - b

    # Instance Method: A method that acts on an instance's attributes (the most common type of method).
    def multiply(self, a, b):
        return a * b

# Using Class Methods and Static Methods
print("\nClass Method (Addition):", Calculator.add(5, 3))
print("Static Method (Subtraction):", Calculator.subtract(9, 4))

# Using Instance Method
calc = Calculator()
print("Instance Method (Multiplication):", calc.multiply(4, 5))

# ----------------------------
# Inheritance (Subclassing)
# ----------------------------

# One of the most important features of OOP is inheritance. A class can inherit attributes and methods from another class.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Another derived class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Creating instances of derived classes
dog = Dog('Buddy')
cat = Cat('Whiskers')

dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.

# ----------------------------
# Special Methods (Magic Methods)
# ----------------------------

# Magic methods (also called dunder methods) are special methods with double underscores.
# They enable custom behavior for built-in operations.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ defines the behavior of the object when printed
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # __len__ allows the use of the len() function on instances of this class
    def __len__(self):
        return self.pages

book = Book('Python Programming', 'John Doe', 300)
print("\nSpecial Methods:")
print(book)  # Calls __str__ method
print("Number of pages:", len(book))  # Calls __len__ method

# ----------------------------
# Class Operations (Instance vs Class)
# ----------------------------

# Checking instance type using isinstance() function
print("\nClass Operations:")
print("Is 'dog' an instance of Animal?", isinstance(dog, Animal))  # True
print("Is 'dog' an instance of Dog?", isinstance(dog, Dog))  # True
print("Is 'dog' an instance of Cat?", isinstance(dog, Cat))  # False

# Checking class inheritance using issubclass() function
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))  # True
print("Is Dog a subclass of Cat?", issubclass(Dog, Cat))  # False

# ----------------------------
# Private and Protected Members
# ----------------------------

# In Python, by convention, a single underscore _ is used to indicate a protected member (intended for internal use),
# while a double underscore __ is used to indicate a private member (not directly accessible).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected variable (by convention)
        self.__bonus = 500  # Private variable (name mangling will be applied)

    def get_salary_with_bonus(self):
        return self._salary + self.__bonus

emp = Employee("John", 3000)

print("\nProtected and Private Members:")
print(f"Employee's salary with bonus: {emp.get_salary_with_bonus()}")
# Accessing the protected member (possible, but not recommended)
print(f"Accessing protected salary: {emp._salary}")

# Accessing the private member (direct access is not allowed, but it can be accessed using name mangling)
# Uncomment the following line to test:
# print(emp.__bonus)  # This will raise an AttributeError

# Correct way to access private variables through name mangling:
print(f"Accessing private bonus: {emp._Employee__bonus}")

