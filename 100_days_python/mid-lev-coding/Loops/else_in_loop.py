# Can a else keyword work with loops ?
for i in range(5):
    print(i)
else:
    print("No more i in loop")
# so yes else works in loops

# Here it will print Empty list
for i in []:
    print(i)
else:
    print("Empty list")
    
# Now tell in below code will the 'else' run after 'break'?
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("No more i in loop")

# So the answer is NO it will break the loop
# Loop will break not it will end successfully 


# same thing with while loop:

i = 0
while i <7:
    print(i)
    i = i+1
    if i ==4:
        break
else:
    print("loop ended")