# The function uses the recursive definition of the sequence to generate the number.
def fibonacci_sequence(num):  
    if num <= 1:
        return num
    else:
        return fibonacci_sequence(num-1) + fibonacci_sequence(num - 2)
    
print(f"The series is", [fibonacci_sequence(i) for i in range(10)])

# The function uses a for loop to generate the sequence iteratively.
def fibonacci_sequence_simple(n : int) -> int:
    
    if n <= 0:
        return []
    # initialize list
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

print("The fibonacci series series is ", fibonacci_sequence_simple(10))