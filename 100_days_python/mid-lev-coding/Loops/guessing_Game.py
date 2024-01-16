# Implement a number guessing game using a while loop. 
# Ask the user to guess a number, and provide hints until they guess correctly.

import random

def guess_number():
    
    secret_num = random.randint(1, 100)
    
    guess = 0
    attempts = 0
    
    print("Welcome to number guessing game")
    print("Try to guess the secret number between 1 to 100, All the best!")
    while guess != secret_num:
        try:
            guess = int(input("Enter a number you wanna guess: "))
            attempts += 1
            
            if guess < secret_num:
                print(f" The {guess} is too low. Try again!")
            elif guess > secret_num:
                print(f"The {guess} is too high. Try again!")
            else:
                print(f"Congrulations!! you guessed it correct")
            print(attempts)
        except ValueError:
            print("You have entered a wrong format")
if __name__ == '__main__':
    guess_number()


