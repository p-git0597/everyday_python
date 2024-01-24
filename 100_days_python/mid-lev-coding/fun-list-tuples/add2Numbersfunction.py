# Write a Python function that takes two parameters (a and b) and returns their sum.

def addTwoNumbers(a, b):
    addition = a + b 
    return addition

try:
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the second number: "))        
    res = addTwoNumbers(a, b)
    print(res)
    
except ValueError:
    print ("Please enter numeric values only")