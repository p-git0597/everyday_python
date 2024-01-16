# Use a while loop to print numbers from 1 to 50 but skip multiples of 5 using the continue statement.

number = 1

while number<=50:
    if number % 5 == 0:
        number += 1
        continue
    else:
        print(number)
        number += 1