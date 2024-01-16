# Use a while loop to calculate the factorial of a given number.

def factorial(number):
    
    # check if the input is not a non-negative number
    if not isinstance(number, int) or number < 0:
        print(" Enter a valid number")
       
    factorial_num = 1
    current_num = 1
    
    while current_num <= number:
        factorial_num = factorial_num * current_num
        current_num += 1
    
    return factorial_num
num = int(input("Enter a number:"))
print(f"The factorial of {num} is",factorial(num))