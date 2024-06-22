# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""


num = float(input("Enter Float Number "))

r_num= round(num,2)

print("The orignal Number : ",num, "The round Number : ",r_num )


chara = input("write a Enter a string:  ")

len_chara = len(chara)

print("The length of the entered string is",len_chara)


# problem 2
"""
Problem Statement:

Prompt the user to enter a sentence.
Convert the entire sentence to uppercase.
Convert the entire sentence to lowercase.
Capitalize the first word of the sentence.

Print each of these modified sentences.
"""

# sol
sentence = input("Enter a sentance : ")

upp_sentence = sentence.upper()
low_sentence = sentence.lower()
cap_sentence = sentence.capitalize()


print("sentence of uppercase ", upp_sentence )
print("sentence of lowercase ", low_sentence )
print("sentence of Capitalize ", cap_sentence )




# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""

# sol


user_sen= input("Enter A Sentence")

print("sentace : ",user_sen)
user_rep= input("Which word you want to replace word ")
user_rep_w = input("Which word you want to replace word with ")

rep_sen= user_sen.replace(user_rep,user_rep_w)

print("replace sentence : ",rep_sen)


# problem 4
"""
Write a program that:
Asks the user to enter their age.
Adds 10 to their age.

Prints a message saying "In 10 years, you will be X years old." where X is the new age.
"""
# sol

user_age = int(input("enter your age"))

# add_user_age += 10
add_user_age = user_age +10

print('"In 10 years, you will be",',add_user_age,'years old." where',add_user_age,' is the new age.')


# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""
# sol

user_full_name = input("Enter your Full Name : ")

upp_user_full_name= user_full_name.upper()

print("full name in Upper case : ",upp_user_full_name)


user_fav_num = int(input("Enter your Favorite number"))
user_fav_num_mul_2 = user_fav_num * 2

message = "Your favorite number multiplied by 2 is " + str(user_fav_num_mul_2) + "."

print(message)


# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))


"""
# sol 
first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")


full_name = first_name + " " + last_name


full_name_upper = full_name.upper()


modified_sentence = full_name_upper.replace(" ", "-")

full_name_length = len(full_name)

print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.
"""
# sol
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average = (num1 + num2) / 2
round_avarage = round(average,2)


print("The average is: ",round_avarage)


# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""
# sol

sentence = input("Enter a sentence: ")

modified_sentence = sentence.replace(" ", "_")

words = modified_sentence.split("_")

print("Modified Sentence:", modified_sentence)
print("Words:", words)
