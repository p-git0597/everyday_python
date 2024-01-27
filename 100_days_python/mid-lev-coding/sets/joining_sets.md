# Joining Sets

Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

## union() and update():

- `union()` method returns a set that contains all items from both sets. It does not modify the original sets.
  The `union()` method returns a set that contains all items from both sets. The `update()` method adds elements from another iterable (such as list, tuple or string) to the set.

## intersection and intersection_update():

The `intersection()` and intersection_update() methods prints only items that are similar to both the sets.
The `intersection()` method returns a new set whereas intersection_update() method updates into the existing set from another set.

## symmetric_difference and symmetric_difference_update():

The `symmetric_difference()` and `symmetric_difference_update()` methods prints only items that are not similar to both the sets. The `symmetric_difference()` method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

## difference() and difference_update():

The `difference` and `difference_update()` methods prints only items that are only present in the original set and not in both the sets. The `difference()` method returns a new set whereas difference_update() method updates into the existing set from another set.

# Set Methods

## isdisjoint():

The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

## issuperset():

The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

## issubset():

The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

## add()

If you want to add a single item to the set use the add() method.

## update()

If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

## remove()/discard()

We can use remove() and discard() methods to remove items form list.

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

## pop()

This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

## del

del is not a method, rather it is a keyword which deletes the set entirely.

What if we don’t want to delete the entire set, we just want to delete all items within that set?

## clear():

This method clears all items in the set and prints an empty set.

## Check if item exists

You can also check if an item exists in the set or not.

Example

```
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```

Output:

```
Carla is present.
```
