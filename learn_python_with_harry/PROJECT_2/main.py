# game guess the number 
import random

number  = random.randint(1, 100)
attempts =1
guess = int(input(" Enter the number you wanna bet on: "))

while(True):
    if(guess > number):
        guess = int(input(f"Guess another number, thsi number {guess} is too big: "))
        attempts += 1
    elif(guess < number):
        guess = int(input(f"Guess another number, thsi number {guess} is too small: "))
        attempts += 1
    else:
        print(f" You guessed it right {guess} is the right number")
        break