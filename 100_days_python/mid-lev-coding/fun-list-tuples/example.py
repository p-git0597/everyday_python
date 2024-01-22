# let's assume we are aksed to calculate Gmean

# Traditional approach:
a = 8
b = 9
# gmean1 = (a*b)/(a+b)
# print(gmean1)

# ## This is a smater move by creating a function:
def gmean(a, b):
    gmean1 = (a*b)/(a+b)
    print(gmean1)
    
# now just calling the function
gmean(8, 9)
gmean(14, 5)


# We are asked to do that same again.
# If we are asked to do this 20 times the time and efforts will be required more to complete
# c = 7
# d = 9
# gmean2 = (c*d)/(c+d)
# print(gmean2)

# now let's assume we are asked to compare a bigger number from both

def isGreater(a,b):
    if a > b :
        print(f"{a} The first number is greater")
    else:
        print(f"{b} The second number is greater")

isGreater(8,7)
isGreater(14, 15)

# We can also leave a function incomplete by adding a pass 
# by which we can come later and complete the function.
### Let's say for example we are asked to compare number is less then other number.

