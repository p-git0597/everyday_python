name = input("Enter your name: ")

if len(name) < 3:
    print(f"You have entered {name}, Name must be more than 3 characters.")
elif len(name) > 50:
    print(f"Name can be a maximum of 50 characters.")
else:
    print(f"Hello!! Name: {name} looks good.")