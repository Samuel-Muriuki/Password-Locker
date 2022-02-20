import random
import string
class Credentials:
    """
    Creating the credentials class
    """
    
    def gen_password():
        """
        Function that generates a random password
        """
        print("Type 't' - to type in your password or 'g' - to auto-generate your password")
        passwrd = input()
        while True:
            
            if passwrd == "t":
                print("Type in your password:")
                passw = input()
                

            elif passwrd == "g":
            
                # Credentials.gen_password
        
                length = int(input("\nEnter the length of password: "))

                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                # symbol = string.punctuation

                all = lower + upper + num #+ symbol

                generate = random.sample(all, length)

                password = "".join(generate)
                print("Your password has been auto-generated\n")
                print(password)
                # Credentials.auto_generated_password.append(password)
                
                
            break
        
    #gen_password()