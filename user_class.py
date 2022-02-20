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
