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

