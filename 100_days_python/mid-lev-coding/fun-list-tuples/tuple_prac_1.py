# Problem 1
# Create a tuple of your favorite colors and print each color.
colors = ("Blue", "White", "Red")

print("My Favourite colors are: ")
for color in colors:
    print(color)

# Problem 2
# Write a program to check if a given element is present in a tuple.

my_tuple = (2, 22, 5, 7, 3, 4, 13, 9)

try:
    num_to_check = int(input("Enter a number to check: "))
    
    if num_to_check in my_tuple:
        print(f"The number {num_to_check} is present in my_tuple")
    else:
        print(f"The number {num_to_check} is not present in my_tuple")

except ValueError:
    print("Invalid input! Please enter an integer.")
