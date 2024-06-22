# Write a program to check whether a person is eligible to vote or not?

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Write a program to check char is vowel or not.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("is a vowel", char)
else:
    print("is not a vowel char", char)

# Write a program to check the number is positive or negative. User input.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Write a program to check whether a number is odd or even?
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
marks = int(input("Enter your marks out of 100: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Write a program to check whether a number is divisible by 7
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("is divisible by 7", num)
else:
    print(" is not divisible by 7", num)


# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" is a leap year", year)
else:
    print("is not a leap year",year)

# Write a program to ask user its name and check whether name consists of 5 or more letters
name = input("Enter your name: ")
if len(name) >= 5:
    print("Name consists of 5 or more letters")
else:
    print("Name consists of less than 5 letters")
# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"

num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by 2 and 3")
elif num % 2 == 0:
    print(f"{num} is only divisible by 2")
elif num % 3 == 0:
    print(f"{num} is only divisible by 3")
else:
    print(f"{num} is neither divisible by 2 nor by 3")

# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger")
elif num2 > num1:
    print(f"{num2} is larger")
else:
    print("Both numbers are equal")


# Write a program that accepts 3 input from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")


# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15
nums = [float(input("Enter first number: ")), float(input("Enter second number: ")), float(input("Enter third number: "))]
nums.sort()
print(f"The second largest number is {nums[1]}")
# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

ignal = input("Enter traffic signal color (red, green, yellow): ").lower()
if signal == 'green':
    print("Car is allowed to go")
elif signal == 'yellow':
    print("Car has to wait")
elif signal == 'red':
    print("Car has to stop")
else:
    print("Invalid input")



"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")

"""
Write a program that takes a password as input and checks its strength:

If the password length is less than 6, print "Weak password".
If the password length is between 6 and 12, print "Moderate password".
If the password length is more than 12, print "Strong password".
"""
password = input("Enter a password: ")
if len(password) < 6:
    print("Weak password")
elif 6 <= len(password) <= 12:
    print("Moderate password")
else:
    print("Strong password")

"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""
salary = float(input("Enter the salary: "))
years_of_service = int(input("Enter years of service: "))

if years_of_service < 5:
    bonus = 0
elif 5 <= years_of_service <= 10:
    bonus = 0.10 * salary
else:
    bonus = 0.20 * salary

print(f"Bonus amount: {bonus}")


"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""
purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount < 100:
    discount = 0
elif 100 <= purchase_amount <= 500:
    discount = 0.10 * purchase_amount
else:
    discount = 0.20 * purchase_amount

final_amount = purchase_amount - discount
print(f"Final amount after discount: {final_amount}")

"""
Write a program that takes a person's age as input and prints the age group they belong to:

If the age is less than 13, print "Child".
If the age is between 13 and 19 (inclusive), print "Teenager".
If the age is 20 or above:
    If the age is less than 65, print "Adult".
    If the age is 65 or above, print "Senior".
"""
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age < 65:
    print("Adult")
else:
    print("Senior")

"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""
membership_status = input("Are you a member? (yes/no): ").lower()
purchase_amount = float(input("Enter the purchase amount: "))

if membership_status == 'yes':
    if purchase_amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
else:
    if purchase_amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")


"""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18

# hint: filename: if_statement/if_with_nested_if.py
"""
age = int(input("Enter your age: "))
affiliated_card = input("Do you have an affiliated card? (yes/no): ").lower()
govt_employee = input("Are you a government employee? (yes/no): ").lower()
grade = int(input("Enter your grade: "))

if age < 60 and affiliated_card == 'yes':
    print("Allowed")
elif govt_employee == 'yes':
    print("Allowed")
else:
    print("Not allowed")

if grade < 18:
    print("Charge 10 Rs more")