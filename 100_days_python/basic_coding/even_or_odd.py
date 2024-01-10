try:
    number1 = int(input("Enter first number: "))

    if number1 % 2 == 0:
        print(f"The given number = {number1} is even")
    else:
        print(f"The given number = {number1} is odd")
        
except ValueError:
    print("Enter a valid Number")