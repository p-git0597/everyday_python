# Excercise:3
# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

# List of questions to ask for the game
questions = [
    ["What is the capital of India?", 'Mumbai', 'New Delhi', 'Kolkata',  'Bangalore', 'None', 2],
    ["Who is the CEO of Microsoft?", "Stephen Ballmer", "Bill Gates", "Larry Ellison", "Mark Zuckerberg", 'None', 2],
    ["Which language was used to create fb?", "Python", "French", "JavaScript","Php", "None", 4],
    ["What is the color of the sun?", 'Yellow', "Red", "Green", "White", 'None', 1],
    ["How many continents are there on Earth?", "One","Eight", "Seven", "Five", "None", 3],
    ["What is the capital of France?", "Paris", "Berlin", "Madrid", "Rome", "None", 1],
    ["Which planet is known as the 'Red Planet'?", "Venus", "Mars", "Jupiter", "Saturn", "Neptune", 2],
    ["What is the largest ocean on Earth?", "Pacific Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean","None", 1],
    ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Baht","None", 3],
    ["In which year did the Titanic sink?", "1905", "1912", "1920", "1931", "None", 2],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "None", 3],
    ["How many sides does a triangle have?", "Three", "Four", "Five", "Six", "None", 1]
    ]
# Level of money upto 50 lakhs
levels = [1000, 3000, 6000, 10000, 25000, 50000, 100000, 320000, 640000, 1250000, 2500000, 5000000]

# Initiating Money with Zero, Let's see if we can be hero in this game
money = 0

for i in range(0, len(questions)):
    
    question = questions[i]
    print(f"\n\n-> Your question for Rs.{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}      b. {question[2]}")
    print(f"c. {question[3]}      d. {question[4]}")
    reply = int(input("Enter your answer from (1-4) or 0 to quit: \n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if i == 3:
            money = 10000
        elif i == 7:
            money = 320000
        elif i == 9:
           money = 1250000
    else:
        print("Your answer is wrong!")
        break
    
print(f"Your final amout you have won is {money}")
        
    