# Combination Calculation
# Write a recursive function to calculate the combination (nCr) of two given numbers.

def combination(n, r):
    
    return fact(n) / (fact(r) * fact(n-r))

def fact(n):
    if n == 0:
        return 1
    res = 1
    
    for i in range(2, n + 1):
        res = res * i
    return res

n = 3
r = 2
print(int(combination(n, r)))