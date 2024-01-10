def factorial(num):
    return 1 if (num == 1) or (num == 0) else num * factorial(num - 1)

num = int(input("Enter a number "))    
print(f"The Factorial of {num} is ",factorial(num))