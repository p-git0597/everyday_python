# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# def average(a, b):
#     print('The average of numbers is ', (a+b)/2)
    
# average(4, 5)

# using tuples in functions

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/ len(numbers)

c = average(3, 4, 3)
print(c)

# using Dictionary

def fullName(**name):
    print(type(name))    
    print("hello,", name['fname'], name['mname'], name['lname'])
    
fullName(mname = 'agrawal', lname = 'patel', fname = 'megha')