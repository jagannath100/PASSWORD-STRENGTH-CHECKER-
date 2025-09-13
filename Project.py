
# password strenghth checker

import re 
# help in searching of special characters

# conditions for strong password min 8  chars, digit, uppercase, lowecase,  special characters


def is_strong_password(password):

    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    
    return "Password is strong and secured ."

def password_checker():
    print("Welcome to the Password Strength Checker!")


    while True:
        password = input("Enter your password (or type 'exit' to quit) : ")

        if password.lower() == 'exit': 
            print("Thank you for using the password strength checker. ")
            break 
     

        result = is_strong_password(password)
        print(result)


if __name__ == "__main__":
    password_checker()


