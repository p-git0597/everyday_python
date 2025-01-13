# #while condition:

# i = 1

# # while i<=5:
# #     print(i)
# #     i += 1
# # print("Done!!")


# while i<=5:
#     print('*' * i)
#     i += 1
# print("Done!!")


# guess = int(input("enter a number to guess: "))
# attempt = 0

# while guess == 9:
#     if guess != 9:
#         print("Try again to guess")
#         attempt += 1
#     if attempt == 3:
#         print("Attempts are ove try after some times")  



secret_number = 9
attempts = 0
attempts_limit = 3
while attempts < attempts_limit:
    guess = int(input("Enter a number to guess: "))
    attempts += 1
    if guess == secret_number:
        print("You guessed it right! you won.")
        break
else:
    print("Your attempts are over. Try again later.")