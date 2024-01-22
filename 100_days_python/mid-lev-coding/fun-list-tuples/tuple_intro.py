# Tuples are ordered collection of data items. They store multiple items in a single variable. 
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])
if  342 in tup:
  print("Yes 342 is present in this tuple")

if  3421 in tup:
  print("Yes 342 is present in this tuple")
else:
    print('3421 Not present')
  

tup2 = tup[1:4]
print(tup2)