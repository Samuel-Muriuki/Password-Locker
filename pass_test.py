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
        
    def test_init(self): # Testing if objects have been inatantiated properly
        """
        Testing for proper object instantiation
        """
        
        self.assertEqual(self.new_user.account_name, "Discord")
        self.assertEqual(self.new_user.login_username, "bot")
        self.assertEqual(self.new_user.password, "Lock-001")
        
    def test_save_user(self):
        """
        Testing if the user object is saved into the user list
        """
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    