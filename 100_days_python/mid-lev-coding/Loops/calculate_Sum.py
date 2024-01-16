# Use a for loop to calculate the sum of all even numbers from 1 to 20.
sum_num = 0
for i in range(1, 21):
    if (i % 2) == 0:
        sum_num = sum_num + i
print(f"The total sum is", sum_num)