#!usr/bin/env python3.9

from user_class import User
from credentials_class import Credentials
import pyperclip


def create_user(acc_name, lgn_username, passwd):
    """
    Function that creates a new user
    """
    new_user = User(acc_name, lgn_username, passwd)
    
    return new_user


def save_users(user):
    """
    Function that saves the new user
    """
    user.save_user()


def find_existing_user(username):
    """
    Function that finds if a user account exists using the username
    """
    return User.find_by_username(username)


def display_users():
    """
    Function that shows all the saved users.
    """
    
    return User.display_users()


def main():
    print("Welcome to the Password Locker App!!!")
    print("\n")

    while True:
        print("Use these short codes to get started:\n acc - Create a new account || disp - Display all users || fnd - Find an existing user account || del - Delete an existing user from the database || cp - Copy password || ext - exit")
        
        short_code = input().lower()

        if short_code == "acc":
            print("New Account")
            print("-" * 20)

            print("Social media account name:")
            acc_name = input()

            print("Username:")
            lgn_username = input()
            
            print("Password:")
            passwd = str(Credentials.gen_password())
            # print(f"Your password is: {password}")

            save_users(create_user(acc_name, lgn_username, passwd))

            print(f"\n New '{acc_name}' Account with '{lgn_username}' as the username created")

            # print("Use these letters to either type in a password or auto-generate one.\n a - Type in your desired password\n b - Get an auto-generated password")

            
            # choose_password = input().lower()
            # while True:
            #     if choose_password == "a":
            #         print("Type in your desired password:")
            #         typed_password = input()

            #     elif choose_password == "b":
            #         print("Your pasword will be autogenerated.")
                    
            #     else:
            #         print("Invalid choice, kindly choose one of the above mentioned")
            
        
        elif short_code == "disp":
            if display_users:
                print("Here is a list of all your accounts:\n")

                for user in display_users():
                    print(f"{user.account_name} {user.login_username} {user.password}")
                    
                    print("\n")

            else:
                print("\n You don't seem to have any accounts yet")
