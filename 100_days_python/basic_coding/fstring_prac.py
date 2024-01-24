    ## String formatting in python
# String formatting can be done in python using the format method.

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

## f-string in python
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String 
# Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of 
# this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be 
# formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python 
# expression inside string literals for formatting.

colour = 'Red'
print(f"My favorite colour is {colour}.")

name = "Ram"
age = 32
print(f"My name is {name} and my age is {age}.")


## if some-one wants to print f-string as it is without inserting a value:
# Add double {{}} and it will print as it is.
print(f"My name is {{name}} and my age is {{age}}.")

# formating the decimal point.
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))
