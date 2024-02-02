# A local variable is a variable that is defined within a function and is only accessible within that function.
# It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible 
# from within any function in your code.

x = 4
print(f"The global var is {x}")

def hello():
    x = 5
    y = 7
    print(f"The local var is {x}")
    print("hello coder")
    print(f"The local var is {y}")
    
    
print(f"The global var is {x}")
hello()
print(f"The global var is {x}")
# # this will cause an error because y is a local variable and is not accessible outside of the function.

# In this example, we have a global variable x and a local variable y. We can access the value of the global variable 
# x from within the function, but we cannot access the value of the local variable y outside of the function.


# The global keyword
# Now, what if we want to modify a global variable from within a function? This is where the global keyword comes in.
# The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. Here's an example:

x = 20 # global variable
print(f"The global var is before changing {x}")
def my_function():
  global x
  x = 10 # this will change the value of the global variable x
  y = 8 # local variable
my_function()
print(f"The global var is {x}") # prints 10
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

# In this example, we used the global keyword to declare that we want to modify the global variable x from within the function.
# It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, 
# as it can lead to unexpected behavior and make your code harder to debug.