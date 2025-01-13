# For Loops
# prices = [10, 20, 30]
# cart_total = 0
# for i in prices:
#     cart_total += i
#     i += 1
# print(f"Total: {cart_total}")

# nested for loops: 
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# Excercise: - 
# 
# numbers = [5, 2, 5, 2, 2]
numbers = [2, 2, 2, 7]

# for x_count in numbers:
#     for y in str(x_count):
#         print("X" * int(y))

for x_count in numbers:
    output = ''
    
    for count in range(x_count):
        output += 'x'
    print(output) 