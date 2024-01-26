# Greatest Common Divisor (GCD) Using Recursion:
# Write a recursive function to find the GCD of two numbers using the Euclidean algorithm.

def gcd(a, b):
    # base case: GCD(a, 0) is a and GCD(0, b) is b
    if b == 0:
        return a
    else:
        # recursion: call gcd with arguments b and remainder of a divided by b
        return gcd(b, a%b)

num1 = 48
num2 = 18
print(gcd(num1, num2))