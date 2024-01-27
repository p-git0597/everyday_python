a = input("Enter a number you want to generate table for: ")

print(f"The multiplication table for {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
   
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"Error occurred: {e}")    

print("Enf of code")