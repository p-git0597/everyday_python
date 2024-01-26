# Write a recursive function to calculate the power of a number, given the base and exponent.

def power_num(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * (base * (exponent-1))
    
try:
    base = int(input("Enter a number u want to get power of: "))
    exponent = int(input("Enter a number u want to assign power "))
    res = power_num(base, exponent)
    print(f"The power of {base} is {res}.")
    
except ValueError:
    print("Invalid input! Please enter a valid integer.")