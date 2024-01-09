# def greet(name = "Ram"):
#     return "Hello " + name

# a = greet()
# print(a)

#recusrion use
# def factorial(n):
#     # base confition
#     if(n == 0 or n == 1):
#         return 1
#     return n * factorial(n-1)

# a = factorial(9)
# print(a)


# def greater(num1, num2, num3):
#     if(num1>num2):
#         greater = num1
#     else:
#         greater = num2
#     if(num3>greater):
#         greater = num3
#     return greater

# print(greater(23,45,2))


# def cel2far(cel):
#     return (cel * 9/5) +32

# print(cel2far(137))

# def sumofNum(n):
#     if(n == 1):
#         return 1
#     return sumofNum(n-1) + n

# print(sumofNum(7))

# def printPattern(n):
#     for i in range(n):
#         print("*"*(n-i))
        
# printPattern(4)

# def process(l, word):
#     word  = word.strip()
#     if word in l:
#         l.remove(word)
#     return l1
 
# l1 = ['harry', 'rohan', 'akash', 'shubham', 'parth']
# print(process(l1, "shubham"))