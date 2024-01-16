# Write a for loop to print all odd numbers from 1 to 15. 
# Use the break statement to stop the loop when encountering the first prime number.
# num = 15
# for i in range(1, num):
#     if (i / 2) != 0:
#         print(i)
#         if (num % i) != 0:
#             break

def is_prime(num):
    
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
for number in range(1, 16, 2):
    print(number)
    
    if is_prime(number):
        print(f"{number} is the first prime number encountered")
        break

# For example, if num is 25, then int(25**0.5) + 1 equals 6. So, when checking for factors, 
# you only need to check up to 6 to determine if 25 is prime. If there are no factors found up to the square 
# root, it implies that there are no factors beyond the square root either, making the number prime. 
