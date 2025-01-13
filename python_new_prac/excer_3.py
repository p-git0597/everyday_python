is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear warn cold")
else:
    print("It's a lovely day")
    
############### Excersice #############
price = int(input("Enter price of the house in millions: "))
credit_score = int(input("Enter the credit score of customer"))

if credit_score > 700:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"The customer has to put down ${down_payment}")