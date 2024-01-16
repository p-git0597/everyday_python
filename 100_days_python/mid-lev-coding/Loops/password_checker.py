# Create a simple password checker using a while loop. 
# Prompt the user for a password until they enter the correct one.

def password_checker():
    
    secret_password = 'Secret1234'
    
    entered_password = ''
    
    print('Welcome to password checker system.')
    
    while entered_password != secret_password:
        entered_password = input(" Enter a password: ")
        
        if entered_password == secret_password:
            print("You have entered correct password")
        else:
            print("Incorrect password, please try again.")
            
if __name__ == '__main__':
    password_checker()
    