# Write a function that uses the recursive definition of the sequence to generate the number. (fibonacci sequence)

def fibonacci_seq(num):
    if num <= 1:
        return num
    else:
        return fibonacci_seq(num-1) + fibonacci_seq(num-2)
print(f"The fibonacci sequence is", [fibonacci_seq(i) for i in range(10)])

