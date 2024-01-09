# f = open("1_dict.py", "r")
# test = f.read()
# print(test)
# f.close()

# f = open("1_dict.py", "r")
# # test = f.read()
# test = f.readlines()
# print(test)
# f.close()
# f = open("write.txt", "a")
# f.write("this is a test\n")
# f.close()

# with open("write.txt", "r") as f:
#     if("this" in f.read()):
#         print("yes this is present")
#     else:
#         print("not present")


# High score

# import random


# def game():
#     score = random.randint(1, 100)
#     print(f"this score is {score}.")
#     return score

# score = game()
# with open("highscore.txt", "r") as f:
#     highscore = int(f.read())
    
# if (highscore<score):
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))

# multiplication tables example 
for i in range(2, 5):
    table = ""
    for j in range(1, 11):
        table += f"{i} X {j} = {i*j}\n"
    with open(f'tables/{i}.txt', 'w') as f:
        f.write(table)