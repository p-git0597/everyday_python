Why do we need function:-

1. To organize our code in a more manageable way.
2. Reusability: Functions allow us to write the same piece of code multiple times with
   different inputs, making it easier to maintain and modify our program as we add features or fix bugs
3. Readability: Functions make our code self-explanatory by giving them meaningful
   names that describe what they do. This makes it easier for other developers (and ourselves) to understand
   what each part of the code does.
4. Modularity: By breaking down our code into functions, we can work on different parts
   of the program independently without having to read through the entire project.
5. Debugging: When something goes wrong in our code, instead of searching through
   hundreds of lines of code, we can use functions to narrow down where the issue is coming
   from.
6. Performance: If certain tasks are performed repeatedly within a system, rather than performing the task
   every time the main routine runs, these tasks should be placed inside a function and called when needed
   so that the computer doesn't have to spend extra cycles doing the same thing over and over.
7. Efficiency: If certain tasks are performed repeatedly throughout our codebase,
   placing those tasks inside a function saves time and resources by avoiding redundant operations.

Functions are particularly useful when working on large projects where dependencies between modules are complex.

## List Methods

list.sort()
This method sorts the list in ascending order. The original list is updated

What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.

The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

reverse()
This method reverses the order of the list.

index()
This method returns the index of the first occurrence of the list item.

count()
Returns the count of the number of items with the given value.

copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

append():
This method appends items to the end of the existing list.

insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

Concatenating two lists:
You can simply concatenate two lists to join two lists.

## Tuples

# Manupilating Tuples

Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)

countries = tuple(temp)
print(countries)

Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
