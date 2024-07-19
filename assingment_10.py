"""
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""
from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

# Example usage
person = Person("pooran", "pakistan", date(1997, 10, 27))
print(person.name + " from " + person.country + " is " + str(person.calculate_age()) + " years old.")


"""
Write a Python program to create a calculator class. Include methods for basic arithmetic operations
"""


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example usage
calc = Calculator()
print("Addition: " + str(calc.add(10, 5)))
print("Subtraction: " + str(calc.subtract(10, 5)))
print("Multiplication: " + str(calc.multiply(10, 5)))
print("Division: " + str(calc.divide(10, 5)))

"""
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
"""
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def calculate_total(self):
        return sum(self.items.values())

# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 50)
print("Total price: " + str(cart.calculate_total()))
cart.remove_item("Mouse")
print("Total price after removing Mouse: " + str(cart.calculate_total()))


"""
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
"""

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, balance=0):
        self.customers[name] = balance

    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name] += amount
        else:
            print("Customer not found!")

    def withdraw(self, name, amount):
        if name in self.customers:
            if self.customers[name] >= amount:
                self.customers[name] -= amount
            else:
                print("Insufficient balance!")
        else:
            print("Customer not found!")

    def get_balance(self, name):
        if name in self.customers:
            return self.customers[name]
        else:
            return "Customer not found!"

# Example usage
bank = Bank()
bank.add_customer("pooran", 1000)
bank.add_customer("rahul", 500)
bank.deposit("Alice", 200)
bank.withdraw("rahul", 100)
print("pooran's balance: " + str(bank.get_balance("pooran")))
print("rahul's balance: " + str(bank.get_balance("rahul")))


"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses

"""

class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def display_info(self):
        print("Name: " + self.name + ", Age: " + str(self.age))

    def enroll(self, course):
        if course in Student.available_courses:
            self.courses.append(course)
            print(self.name + " has enrolled in " + course)
        else:
            print("Course " + course + " is not available.")

    def list_courses(self):
        print(self.name + " is enrolled in: " + ", ".join(self.courses))

    @staticmethod
    def list_available_courses():
        print("Available courses: " + ", ".join(Student.available_courses))


# Creating three instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Enrolling the students in courses
student1.enroll("Math")
student1.enroll("Physics")
student2.enroll("English")
student2.enroll("Islamyat")  # This should not be allowed
student3.enroll("Chemistry")
student3.enroll("Urdu")

# Listing the courses each student is enrolled in
student1.list_courses()
student2.list_courses()
student3.list_courses()

# Listing all available courses
Student.list_available_courses()
