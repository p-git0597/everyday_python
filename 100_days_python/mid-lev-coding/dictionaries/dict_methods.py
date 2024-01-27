emp1 = {122: 45, 137: 50, 131: 100, 127: 23}
emp2 = {144: 50, 147: 31}

# emp1.update(emp2)
# print(emp1)

# emp2.clear()
# print(emp2)

# emp1.pop(122)
# print(emp1)

# emp1.popitem()
# print(emp1)

# del emp1 -> If key is not provided, then the del keyword will delete the dictionary entirely.
del emp1[131]
print(emp1)