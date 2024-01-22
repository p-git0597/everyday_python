tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = list(tuple1)
print(res)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)

res = tuple1.index(31)
print(res)

res = tuple1.index(3, 4, 8)
print(res)
res = len(tuple1)
