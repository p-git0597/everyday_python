# i  = 1
# while(i<6):
#     print(i)
#     i+=1

# a = [1,'appple',3,5,6,"banana"]
# i = 0
# while(i<len(a)):
#     print(a[i])
#     i+=1
    
# a = [1,'appple',3,5,6,"banana"]
# i = 0   
# # for i in range(len(a)):
# #     print(a[i])
# #     i+=1

# for items in a:
#     print(items)

# a = [1,'appple',3,5,6,"banana"]
# for item in a:
#     print(item)
#     if(item ==3):
#         continue
#     print("this is printed")
# print("end")


# num  = int(input("ENter number here\n"))
# for i in range(10):
#     print(f"{num}X{i+1} = {num*(i+1)}")


# l = ["sam", "som", "ram", "Sham"]

# for item in l:
#     if item.startswith("s"):
#         print(f"Good mornig {item}")


# num = 3

# for i in range(2, num):
#     if(num%i) == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# i = 1
# sum  = 0
# n = 3
# while(i<=n):
#     sum+=i
#     i+=1
# print(f"usm is {sum}")


# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2*i-1):
#         print("*", end="")
#     for j in range(n-i):
#         print(" ", end="")
#     print("\n", end="")


# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n", end="")

n= 10
for j in range(1, 11):
    i = 11 - j
    print(f"{n} X {i} = {n*i}")