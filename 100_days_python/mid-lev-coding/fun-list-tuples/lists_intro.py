# creating a list
marks = [3, 5, 6, 'Sam', True, 6, 8, 45, 67, 7, 4, 90, 56]

# Lets play around with 'print' list marks in diffrent ways

print(marks)
# print(marks[0])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
print(len(marks))

# let's try it with negative index
print(marks[-1])

# let's simplify the -ve index confusion
# so -ve index is genrally (len(variable) - index) let's see it with example
# you will notice allt eh values below are same as index -1

print(marks[len(marks) - 1])
print(marks[13- 1])
print(marks[12])

# let's see how to check if a particular value is present in the list or not
if 'Sam' in marks:
    print("Yes, Sam is present")
else:
    print("No, Sam is not present")
    
# now we will try slicing:
print(marks[:]) # this will print all the elements in general this is telling print(0:13) as we haven't mentioned anything.
print(marks[1:6]) 
print(marks[1:10:2]) # here we are specifying we want list from 1 to 10 but skip it by position 2
# this means every second element starting from first.


## IMP topic 
# List Comprehension

lst = [i for i in range(7)]
print(lst)
# Applying condition to the list comprehension.
lst1 = [i * i for i in range(10) if i%2==0]
print(lst1)

