# option = input("> ")

# while option == "help":
#     print(""" start - to start the car \n stop - to stop the car \n quit - to exit""")
#     command = input(">")
#     if command.lower() == "start":
#         print("car has started! let's gooo ...---...")
#     elif command.lower() == "stop":
#         print("Car has stopped. :(")
#     elif command.lower() == "exit":
#         print("we are out now")
#         break
# else:
#     print("Enter a valid input")

command = ''

started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("car has started! let's gooo ...---...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car has stopped. :(")
    elif command == "help":
        print(""" start - to start the car \n stop - to stop the car \n quit - to exit""")
    elif command == 'quit':
        break
    else:
        print("Enter a valid input")
