# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

l = [100, 200, 300, 400]

for index, value in enumerate(l):
    print(index, value)

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop


l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']

common_count = {}
for value in l1 + l2:
    if value in common_count:
        common_count[value] += 1
    else:
        common_count[value] = 1

print(common_count)

# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"
x = 2783
counter = 0

while x > 0:
    counter += 1
    x = x // 10

print(counter)

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”
while True:
    user_input = input("Enter something (enter 0 to stop): ")
    if user_input == '0':
        break
    print(f"You entered: {user_input}")

# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list
numbers = []
count = 0

while count < 5:
    number = int(input("Enter a number: "))
    numbers.append(number)
    count += 1

print("Sum of all numbers:", sum(numbers))

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
while True:
    name = input("Enter a name (enter END to stop): ")
    if name == "END":
        break
    print(f"You entered: {name}")

print("I am done.")
# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"
l1 = [11, 33, 50]
result = ""
for num in l1:
    result += str(num)

print(result)
# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

words = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']

for word in words:
    if len(word) > 5:
        print(word)





# nested loop
# check folder class_7/nested_loop_assignment/






# functions

# Write a program to create a function that takes two arguments, name and age. print them inside function.

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Alice", 30)
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=9000):
    print(f"Employee Name: {name}, Salary: {salary}")

show_employee("John")
show_employee("Doe", 12000)

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]
def create_list(*args):
    return list(args)

a = 4
b = 8
c = 10
d = 12
print(create_list(a, b, c, d))

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.
def km_to_miles(km):
    return km * 0.621371

print(km_to_miles(10))
# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.
def is_divisible_by_11(number):
    return number % 11 == 0

print(is_divisible_by_11(22))
print(is_divisible_by_11(23))
# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.
def get_highest(num1, num2):
    return max(num1, num2)

print(get_highest(10, 20))
# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.

def fuel_cost(distance, fuel_per_liter=280):
    return distance * fuel_per_liter

print(fuel_cost(50))
print(fuel_cost(50, 300))
# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false
def is_valid_email(email):
    if len(email) > 256:
        return False
    if not (email[0].isalnum()):
        return False
    if '@' not in email:
        return False
    local, domain = email.split('@', 1)
    if '.' not in domain:
        return False
    if not local:
        return False
    if not domain.split('.', 1)[0]:
        return False
    if not domain.split('.')[-1]:
        return False
    return True

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid.email@com"))

"""
Take a variable store i.e
Store = {“name”: “my store”, “inventory”: [], “orders”: []}

Add 5 items in the inventory using a function “add_item”
id, name, price and quantity

Take user input unless it says “done”
Display user updated inventory items every time
Ask user to type id of the item to purchase or type “done” to checkout
Each time only 1 quantity will by subtracted from the item

Functions: add_item_in_inventory, add_item_in_basket(), checkout()
On checkout, print “{quantity} {item} sold in {store}”
"""
store = {"name": "my store", "inventory": [], "orders": []}

def add_item_in_inventory(item_id, name, price, quantity):
    store["inventory"].append({"id": item_id, "name": name, "price": price, "quantity": quantity})

def add_item_in_basket(item_id):
    for item in store["inventory"]:
        if item["id"] == item_id and item["quantity"] > 0:
            item["quantity"] -= 1
            store["orders"].append(item)
            print(f"Added {item['name']} to basket.")
            return
    print("Item not found or out of stock.")

def checkout():
    print(f"{len(store['orders'])} items sold in {store['name']}.")
    store["orders"].clear()

# Add 5 items to the inventory
add_item_in_inventory(1, "Apple", 100, 10)
add_item_in_inventory(2, "Banana", 50, 20)
add_item_in_inventory(3, "Orange", 80, 15)
add_item_in_inventory(4, "Mango", 150, 5)
add_item_in_inventory(5, "Grapes", 120, 12)

# User interaction for purchasing items
while True:
    print("Current Inventory:", store["inventory"])
    user_input = input("Enter item ID to purchase or 'done' to checkout: ")
    if user_input.lower() == "done":
        break
    try:
        item_id = int(user_input)
        add_item_in_basket(item_id)
    except ValueError:
        print("Invalid input. Please enter a valid item ID or 'done'.")

checkout()
