# If-Else Statements:
# Write a program to check if a number is positive, negative, or zero using if-else statements.

def num_check(num):
    """This function takes an input number and checks whether it's positive, negative, or zero"""
    
    if num > 0:
        print(f"The number {num} is positive")
    elif num < 0:
        print(f"The number {num} is negative")
    else:
        print(f"The number {num} is zero")

# Test the function with different numbers
try:
    num = int(input("Enter a number "))
# unnecessaryily stored the value in res i could have called the function directly
    # res = num_check(num)
    # print(res)
    
    num_check(num)
except ValueError:
    print("Please enter a valid integer input")