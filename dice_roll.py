import random

computer_dice_roll = random.randint(1, 6)
gamer_dice_roll = int(input("Enter your dice roll (1-6): "))

if gamer_dice_roll < 1 or gamer_dice_roll > 6:
    print("Invalid input! Please enter a number between 1 and 6.")
elif gamer_dice_roll == computer_dice_roll:
    print("You guessed it right! The computer rolled a", computer_dice_roll)
else:
    print("You guessed wrong! The computer rolled a", computer_dice_roll)