def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
        
try:
    n = int(input("Enter a number "))
    
    if prime_number(n):
        print(f"The given number {n} is prime number")
    else:
        print(f"The given number {n} is not prime number")

except ValueError:
    print(" Enter a valid int number")