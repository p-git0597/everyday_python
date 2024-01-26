# Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are 
# separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change 
# items of the set once created. Sets do not contain duplicate items.

s = {2, 4, 6, 3, 2, 5}
print(s)

# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers.
# Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is 
# a set?

p = {}
print(type(p)) # -> Here you will see as it prints dict, Yes that the wrong way to create empty set.
 # Here is the right way to create SET.
s1 = set()
print(type(s1))

# Accessing set items:
# Using a For loop
# You can access items of set using a for loop.

info = {"Sam", 19, True, 1.5}
for items in info:
    print(items)