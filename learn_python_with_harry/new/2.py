# Weight from Kg to LBS

weight = float(input("Enter your weight: "))
option = input("Enter (L) for LBS or (K) for KG: ")


# My Solution
# if (option == "L" or option == "l"):
#     new_weight = weight / 2.2046
#     print(f"The weight in LBS: {new_weight}")
# elif(option == "K" or option == "k"):
#     new_weight = weight * 2.2046
#     print(f"The weight in KG: {new_weight}")
# else:
#     print("Enter a correct option L or K")


## optimized:

if option.upper() == "L":
    new_weight = weight / 2.2046
    print(f"The weight in LBS: {new_weight}")
elif option.upper() == "K" :
    new_weight = weight * 2.2046
    print(f"The weight in KG: {new_weight}")
else:
    print("Enter a correct option L or K")