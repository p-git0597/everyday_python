##### Joining Sets #####
# union() and update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities)
cities3 = cities.union(cities2)
print(cities3)

## commenting as to not update the cities 
# cities.update(cities2)
# print(cities)

# intersection and intersection_update():
cities4 = cities.intersection(cities2)
print(cities4)

## commenting as to not update the cities2 
# cities2.intersection_update(cities)
# print(cities2)

# symmetric_difference and symmetric_difference_update():
cities5 = cities.symmetric_difference(cities2)
print(cities5)

## commenting as to not update the cities
# cities.symmetric_difference_update(cities2)
# print(cities)

# difference() and difference_update():
cities6 = cities.difference(cities2)
print(cities6)

## commenting as to not update the cities2 
# cities2.difference_update(cities)
# print(cities)

##### Set Methods #####

# isdisjoint()
print(cities.isdisjoint(cities2))

# issuperset():
print(cities.issuperset(cities2))
print(cities.issuperset(cities4))

# issubset():
print(cities.issubset(cities2))

# add()
cities.add("Mumbai")
print(cities)

# update():
cities.update({"Delhi", "Bangalore", "Hyderabad"})
print(cities)

# remove()/discard():
# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# pop()
city = cities.pop()
print(city)


# del

# cities10 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities10
# print(cities10)

# clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists
# You can also check if an item exists in the set or not.

# Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
