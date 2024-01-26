# Recursion in python
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call 
# itself. These types of construct are termed as recursive functions.

# Let's see the example for Factorial:
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num -1)
    
try:
    num = int(input("Enter a number for factorial calculation: "))
    res = factorial(num)
    print(f"The factorial of {num} is {res}.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")