og_string = input("Enter a text you want to reverse ")
rev_string = ''

for char in og_string:
    rev_string = char + rev_string

print("the reverse is", rev_string)
