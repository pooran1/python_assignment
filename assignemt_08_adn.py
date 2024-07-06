
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

if __name__ == "__main__":
    main()







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

if __name__ == "__main__":
    main()


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

if __name__ == "__main__":
    main()
