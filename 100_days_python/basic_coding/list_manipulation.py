import random 

# Manually creating list elements
list_1 = [ 3 , 7, 90, 45, 23, 23, 1, 48]

# using random.sample()
list1 = random.sample(range(1, 101), 10)
print(list1)

# using random.randint()
my_list = []
for i in range(10):
    my_list.append(random.randint(1, 50))
print(my_list)


sum_list = sum(list1)
print(f"The sum of all the vales in list is ", sum_list)
print(f"The max value from list is ", max(list1))
print(f"The min value from list is ", min(list1))
print(f"The avg value from list is ", sum_list / len(list1))

