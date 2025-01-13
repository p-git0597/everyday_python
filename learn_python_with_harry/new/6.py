# Lists

names = ['jhon', 'Bob', 'Mosh', 'Sarah', "Maria"]
# print(names)
# print(names[1])
# print(names[-1])
# print(names[-2])
# print(names[2:])
# print(names[2:4])
# print(names[:])

# Write a program to find the largest number in a list.
list_1 = [2, 65, 34, 24, 74, 64, 77]

max_num = list_1[0]

for i in list_1:
    if i > max_num:
        max_num = i
print(max_num)


