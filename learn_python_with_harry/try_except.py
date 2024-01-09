# try:
#     with open('1.txt', 'r') as f:
#         f.read()
#     with open('1.txt', 'r') as f:
#         f.read()
#     with open('1.txt', 'r') as f:
#         f.read()
# except Exception as e:
#     print(f"The file is not processing Reason: {e}")
    

# list =[1,2,3,4,5,6,7,8,9,10]

# for index, item in enumerate(list):
#     if(index + 1 == 3 or index +1 == 5 or index +1 ==7):
#         print(item)

num = int(input("Enter a number: "))

multi = [i*num for i in range(1,11)]
print(multi)