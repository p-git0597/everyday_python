# Define a function that calculates the area of a circle given its radius.
import math

def areaOfCircle(r):
    # Checkk if the radius is non-negative
    if r < 0:
        return "Please enter a non-negative number for radius."
    
    area = math.pi * r * r
    return area

try:
    r = int(input("Enter the radius of circle: "))
    res = areaOfCircle(r)
    print(f"The area of circle is {res}.")

except ValueError:
    print("Enter a valid radius value")
