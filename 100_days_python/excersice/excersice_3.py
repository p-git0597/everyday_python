# Excercise:3
# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

# import random

# def kbc_game():
#     final_amount = 0
#     amount = 1000
#     guess = []
#     print("Welcome to Kon Banega Crorepati!!!!")
    
#     question_ans = {'What is the capital of India?': ['New Delhi'], 
#                 'How many continents are there on Earth?': ['Seven'],
#                 'What is the color of the sun?': ['Yellow'],
#                 'What is the capital of the United States?': ['Washington, D.C'],
#                 'How many legs does a cat have?': ['Four']}
    
#     while guess != question_ans.values():
#         q_key = random.choice(list(question_ans.keys()))
#         guess = input("Enter a answer you thivk it can be ")
#         if guess in question_ans[q_key]:
#             print("Correct answer")
#             final_amount = final_amount + amount
#             print("Your current amount is ",final_amount)
#         else:
#             print("Incorrect answer")
#             break
#         return f"You have won {final_amount}"
#     if __name__ == "__main__":
#         print(kbc_game())