number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 :
    print(f"Number1= {number1} is greater then {number2}, {number3}")
elif number3 > number2 :
    print(f"Number3 = {number3} is greater then {number1}, {number2}")
else:
    print(f"Number2 = {number2} is greater then {number1}, {number3}")
