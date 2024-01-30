# Python - else in Loop

## can be asked in Interview.

As you have learned before, the `else` clause is used along with the `if` statement.

Python allows the `else` keyword to be used with the for and `while` loops too. The `else` block appears after the body of the loop. The statements in the `else` block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

Syntax

```
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```

Example:

```
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
```

Output:

````
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop```
````

## Enumerate function in python

The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

## Loop over a list and print the index and value of each element

```
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

The output of this code will be:

```
0 apple
1 banana
2 mango
```

As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

## Loop over a list and print the index (starting at 1) and value of each element

```
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

This will output:

```
1 apple
2 banana
3 mango
```

The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

```
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
```

This will output:

```
1: apple
2: banana
3: mango
```
