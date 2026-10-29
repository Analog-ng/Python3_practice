
import random
 
computer_choice = random.choice(['rock', 'paper', 'scissors'])
User_input = input("Enter your choice (rock, paper, scissors): ")

if User_input == computer_choice:
    print("It's a tie!")
elif (User_input == 'rock' and computer_choice == 'scissor') or (User_input == 'paper' and computer_choice == 'rock') or (User_input == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")