import unittest

import pyperclip  # Importing the unittest module
from user_class import User # Importing the contact class


class TestUser(unittest.TestCase):
    """
    Test case that defines the user class behaviours.

    Args:
        unittest.TestCase: The TestCase class helps in creating the test class.
    """
    
    def setUp(self):
        """
        Set up method runs before each test case
        """
        
        self.new_user = User("Discord", "bot", "Lock-001") # Creating the user object
        
    
    def tearDown(self):
        """
        tearDown method cleans up after each test case has been run.
        """
        
        User.user_list = []