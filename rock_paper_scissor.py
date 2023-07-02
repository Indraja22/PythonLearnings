import random
import sys

computer_choice = random.choice(["rock", "paper", "scissor"])
computer_wins = 0
user_wins = 0

while True:
    user_choice = input("Choose between rock, paper and scissor OR Type 'Q' to quit : ")

    if user_choice.lower() == 'q':
        sys.exit()

    if user_choice not in ['rock', 'paper', 'scissor']:
        print("You choose an incorrect option!")
        continue

    print(f"Computer choice is : {computer_choice}")

    if computer_choice.lower() == user_choice.lower():
        print("There is a draw!")
    elif (computer_choice == 'rock' or computer_choice == 'scissor') and user_choice == 'paper':
        print("Computer wins!")
        computer_wins += 1
    elif computer_choice == 'rock' and user_choice == 'scissor':
        print("Computer wins!")
        computer_wins += 1
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print("User wins!")
        user_wins += 1
    elif (user_choice == 'rock' or user_choice == 'scissor') and computer_choice == 'paper':
        print("User wins!")
        user_wins += 1
    print(f"User scored {user_wins} and Computer scored {computer_wins}")
