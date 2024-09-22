light = input("Enter the light you see:")

if (light == "Red" or light == "red"):
    print("You have to Stop.")
elif (light == "Yellow" or light =="yellow"):
    print("You have to yeild and proceed with caution.")
elif (light == "Green" or light == "green"):
    print("You are good to go. Speed limit 35 mph.")
else:
    print("The signal is broken proceed with caution and report the issue on our website.")
    


# Clever if/ Ternary Operator: - 
# <Var> = (false_val, true_val) [<condition>]

age = int(input("age: "))
vote = ("yes", "no") [age<18]
print(vote)