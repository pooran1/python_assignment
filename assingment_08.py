# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content


# Function to create and update the text file
def update_user_email(user, title, link):
    # Initial content with placeholders
    initial_content = """
    Hi *user*!

    We've found the best article for you based on your interest: *title*
    Please click *here* to open the article
    """

    # Replace placeholders
    updated_content = initial_content.replace('*user*', user).replace('*title*', title).replace('*here*', link)

    # Write updated content to the user_email.txt file
    with open('user_email.txt', 'a') as file:
        file.write(updated_content + "\n")

# Run the function three times with different values
update_user_email('Alice', 'How to Learn Python', 'www.learnpython.com')
update_user_email('Bob', 'Understanding Odoo', 'www.odoo.com')
update_user_email('Carol', 'Mastering Django', 'www.djangomastery.com')



# Create a new text file named "student_records.txt" with the following initial content:
# Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# Open "updated_records.txt" in append mode('a') and add a new student record:
# Close the "updated_records.txt" file.

# Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.


# Step 1: Create student_records.txt with initial content
with open('student_records.txt', 'w') as file:
    file.write("Student ID | Student Name | Grade\n")
    file.write("101       | Alice        | A\n")
    file.write("102       | Bob          | B\n")
    file.write("103       | Carol        | C\n")

# Step 2: Read and print the contents of student_records.txt
with open('student_records.txt', 'r') as file:
    print(file.read())

# Step 3: Create updated_records.txt with specific grades
with open('student_records.txt', 'r') as read_file, open('updated_records.txt', 'w') as write_file:
    lines = read_file.readlines()
    write_file.write(lines[0])  # Write header
    for line in lines[1:]:
        if 'A' in line or 'B' in line:
            write_file.write(line)

# Step 4: Append a new student record to updated_records.txt
with open('updated_records.txt', 'a') as file:
    file.write("104       | Dave         | B\n")

# Step 5: Read and print the contents of updated_records.txt
with open('updated_records.txt', 'r') as file:
    print(file.read())


#########################
#########################
#########################

"""
### Assignment: Password Manager Program
Demo: https://www.youtube.com/watch?v=O8596GPSJV4

#### Objective:
Create a password manager program that allows users to store, retrieve, and manage their passwords. 
The program will use file handling to save and read data, and it will be run in the terminal.

#### Requirements:
1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
3. **Basic Operations**:
    - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
    - **Retrieve a password**: Ask for the website and return the username and password.
    - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

#### Program Flow:
1. Display a menu with the following options:
    - Add a new password
    - Retrieve a password
    - Delete a password
    - Exit
2. Based on the user's choice, perform the corresponding operation.
3. Repeat the menu until the user chooses to exit.







#### Detailed Instructions:
1. **Menu Display**: Create a function to display the menu and get the user's choice.
2. **Add Password**:
    - Prompt the user for the website, username, and password.
    - Write this information to a file in a structured format.
3. **Retrieve Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Display the username and password.
4. **Delete Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Remove the entry and update the file.
5. **File Format**: Store each entry in a new line in the format:
    ```
    website,username,password
    ```

#### Example:
1. **Add Password**:
    ```
    Enter website: example.com
    Enter username: user1
    Enter password: pass123
    Password saved successfully!
    ```
2. **Retrieve Password**:
    ```
    Enter website: example.com
    Username: user1
    Password: pass123
    ```
3. **Delete Password**:
    ```
    Enter website: example.com
    Password deleted successfully!
    ```

#### Hints:
- Use functions to keep your code organized.
- Use lists and dictionaries to manage the data in memory before writing to or reading from the file.
- Ensure to handle cases where the file may not exist initially.

#### Additional Notes:
- Focus on functionality rather than security for this assignment.
"""

"""
create the same program again but this time file data should be stored in json
"""

"""
create the same program again but this time file data should be stored in binary using pickle module

"""

# Part 1: Using Plain Text Files
import os

def display_menu():
    print("\nPassword Manager")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    return input("Choose an option: ")

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open('passwords.txt', 'a') as file:
        file.write(f"{website},{username},{password}\n")
    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    if not os.path.exists('passwords.txt'):
        print("Password file does not exist.")
        return
    with open('passwords.txt', 'r') as file:
        for line in file:
            stored_website, username, password = line.strip().split(',')
            if stored_website == website:
                print(f"Username: {username}")
                print(f"Password: {password}")
                return
    print("Website not found.")

def delete_password():
    website = input("Enter website: ")
    if not os.path.exists('passwords.txt'):
        print("Password file does not exist.")
        return
    updated_lines = []
    with open('passwords.txt', 'r') as file:
        for line in file:
            if not line.startswith(website):
                updated_lines.append(line)
    with open('passwords.txt', 'w') as file:
        for line in updated_lines:
            file.write(line)
    print("Password deleted successfully!")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()

# Part 2: Using JSON Files

import json
import os

def display_menu():
    print("\nPassword Manager")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    return input("Choose an option: ")

def load_passwords():
    if not os.path.exists('passwords.json'):
        return {}
    with open('passwords.json', 'r') as file:
        return json.load(file)

def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords = load_passwords()
    passwords[website] = {'username': username, 'password': password}
    save_passwords(passwords)
    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    passwords = load_passwords()
    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("Website not found.")

def delete_password():
    website = input("Enter website: ")
    passwords = load_passwords()
    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Website not found.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()


# Part 3: Using Pickle for Binary Files


import pickle
import os

def display_menu():
    print("\nPassword Manager")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Delete a password")
    print("4. Exit")
    return input("Choose an option: ")

def load_passwords():
    if not os.path.exists('passwords.pkl'):
        return {}
    with open('passwords.pkl', 'rb') as file:
        return pickle.load(file)

def save_passwords(passwords):
    with open('passwords.pkl', 'wb') as file:
        pickle.dump(passwords, file)

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords = load_passwords()
    passwords[website] = {'username': username, 'password': password}
    save_passwords(passwords)
    print("Password saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    passwords = load_passwords()
    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("Website not found.")

def delete_password():
    website = input("Enter website: ")
    passwords = load_passwords()
    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Website not found.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()


