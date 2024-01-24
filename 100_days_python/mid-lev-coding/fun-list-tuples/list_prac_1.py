# Create a list of fruits and use a list method to add "Banana" to the end of the list.
fruit_list = ["Mango", "Grapes", "Apple", "Cherries"]
item_to_add = ["Banana"]

fruit_list.extend(item_to_add)
print(fruit_list)
#        OR            #
# fruit_list.append(item_to_add)
# print(fruit_list)