my_list = [11,4,5,6,7,34,63,66,24, 4, 6, 4, 7]
print(my_list)
# Method append:
my_list.append(34)

# let's sort our list
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

list1 = ['Ami', 'Sampu', 'Mumbai', 101, 100]
print(list1.index('Sampu'))
print(my_list.index(34))

print(my_list.count(4))

m = my_list.copy()
m.append(1232)
print(m)

my_list.insert(1, "USA")
print(my_list)


my_list.extend(list1)
print(my_list)

# concate 2 list
print(my_list + list1)