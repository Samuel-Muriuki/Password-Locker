import pyperclip


class User:
    """
    Class that generates new instances of a user
    """
    
    user_list = [] 
    
    def __init__(self, account_name, login_username, password):
        
        """
        __init__ method helps us define properties for our objects
        
        Args:
        account_name: The name of the socila account
        login_username: The name of the user associated with the account.
        password: The authentication key
        """
        
        self.account_name = account_name
        self.login_username = login_username
        self.password = password


    def save_user(self):
        """
        save_user method saves the user object in the contact list
        """
        
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes user object from the contact list
        """
        
        User.user_list.remove(self)
        


    @classmethod
    def find_by_username(cls, username):
        """
        Method that takes a username and returns the account that matches that username.

        Args:
            username: The account username to search for.
        
        Returns: 
            Account of person matching the username.
        """
        
        for user in cls.user_list:
            if user.login_username == username:
                return user
            
