def is_aleap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year %  400 == 0):
        return True
    else:
        return False
try:    
    number1 = int(input("Enter a number: "))

    if is_aleap_year(number1):
        print(f"The Number = {number1} is a leap year")
    else:
        print(f"The Number = {number1} is not a leap year")

except ValueError:
    print("Please enter a valid year")