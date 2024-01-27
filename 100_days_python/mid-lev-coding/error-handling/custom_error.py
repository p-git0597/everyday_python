# Here I made mistake.
# class CustomError(Exception):
#     def CustomError(a):
#         if a == 'quit':
#             return True
#         else:
#             return False
# try:
#     inp_string = input("Enter a string for validation: ")
#     if inp_string == 'quit':
#         print(f"As per the {{inp_string}} we have now exited.")

# except CustomError:
#  print("Enter a valid string in input")
############################################################################
# The correct solution is here

class CustomError(Exception):
    pass

def validate_string(input_string):
    if input_string.lower() == 'quit':
        return True
    else:
        raise CustomError("Invalid Input. Enter a valid string.")
try:
    input_string = input("Enter a string you want to check: ")
    if validate_string(input_string):
        print("You entered quit, so program has been closed.")
except CustomError as ce:
    print(ce)
    
# Some Explanation for the code:
# I defined a CustomError class inheriting from Exception.
# I created a separate function validate_input to check if the input is 'quit'. If it is, it returns True, otherwise, it raises a CustomError.
# I used the lower() method to make the comparison case-insensitive.
# In the except block, I catch the CustomError and print the error message.
# Now, this code will raise a custom error if the input is anything other than 'quit'.






