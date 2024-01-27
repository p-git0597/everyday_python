## Set Creation:
# Create an empty set and print its type.
empty_set = set()
print(type(empty_set))

# Initialize a set with elements "apple," "banana," and "cherry."
s = {'apple', 'banana', 'cherry'}
print(s)
print(type(s))

## Adding and Removing Elements:
# Add "orange" to the set created in question 1.
s1 = {'apple', 'banana', 'cherry'}
s1.add('orange')
print(s1)

# Remove "banana" from the set.
s2 = {'apple', 'banana', 'cherry'}
s2.remove('banana')
print(s2)

## Set Operations:
# Create two sets: one with even numbers up to 10 and another with multiples of 3 up to 10. 
# Perform a union of these sets.
s_even = {2,4,6,8,10}
s_odd = {3,6,9}
s_nums = s_even.union(s_odd)
print(s_nums)

# Find the intersection of the two sets from the previous question.
s_nums_intersection = s_even.intersection(s_odd)
print(s_nums_intersection)


## Checking Membership:
# Create a set with a few colors. Check if "red" is present in the set.
colors = {'Blue', 'White', 'Yellow', 'Green'}
if 'Red' in colors:
    print("The Red color is present")
else:
    print("The Red color is not present")
# Check if "green" is present in the set.
if 'Green' in colors:
    print("The Green color is present")
else:
    print("The Green color is not present")
    
## Set Methods:
# Use the clear() method to empty a set.
fruits = {"Apple", "Banana", "Orange"}
fruits.clear()
print(fruits)

# Use the copy() method to create a shallow copy of a set.
fruits = {"Apple", "Banana", "Orange"}
vegetables = fruits.copy() #shallow copy
print(vegetables)

## Difference and Symmetric Difference:
# Create two sets with some overlapping elements. Find the elements that are unique to each set using the 
# difference() method.
s3 = {2, 3, 4, 7, 8, 10, 15, 20}
s4 = {3, 12, 4, 18, 20, 7}
s5 = s3.difference(s4)
print(s5)
# Find the symmetric difference between the two sets.
s6 = s3.symmetric_difference(s4)
print(s6)

# Subset and Superset:
# Create two sets, one with numbers 1 to 5 and another with numbers 1 to 10. Check if the first set is a 
# subset of the second.
num1 = {1,2,3,4,5}
num2 = {1,2,3,4,5,6,7,8,9,10}
print(num1.issubset(num2))
# Check if the second set is a superset of the first.
print(num2.issubset(num1))

# Set Comprehension:
# Create a set containing the squares of numbers from 1 to 5 using set comprehension.
# s = set()
# {s.add(i * i) for i in range(1, 6)}
# print(s)
s= {i**2 for i in range(1, 6)}
print(s)


## Discard and Remove Methods:
# Create a set with a few elements. Use the discard() method to remove an element that may or may not be in the set.
num = {1,2,3,4,5}
num.discard(3)
num.discard(7)
print(num)
# Use the remove() method to remove an element that is definitely in the set.
# num.remove(7) # -> KeyError: 7
num.remove(2)
print(num)

## Frozen Sets:
# Create a frozen set with a few elements and try to add an element to it.

# my_set = frozenset({1,3,5,10,8,9,})
# my_set.add(15)
# print(my_set)

# In this example, the attempt to add an element using the add method will raise an AttributeError because 
# frozen sets do not support modification operations like adding or removing elements. 
# The frozen set remains unchanged after the attempted addition.