# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string
# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
from random import choice
from string import ascii_lowercase
st = input("Enter a string ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding == '1') else False
print(coding)
if (coding):
    nwords = []
    for word in words:
        if(len(word) >=3):
            # r1 = input("Enter first random characters you want to add: ")
            # r2 = input("Enter second random characters you want to add: ")
            r1 = ''.join([choice(ascii_lowercase) for _ in range(3)])
            r2 = ''.join([choice(ascii_lowercase) for _ in range(3)])
            newword = r1 + word[1:] + word[0] + r2
            nwords.append(newword)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word) >=3):
            newword = word[3:-3]
            newword = newword[-1] + newword[:-1]
            nwords.append(newword)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))