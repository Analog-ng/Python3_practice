import random

def dice_roll():
    #Simulates rolling a six-sided die and returns the result.
    return random.randint(1, 6) + random.randint(1, 6)
def main():
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")

    player1_score = dice_roll()
    player2_score = dice_roll()

    print(f"{player1} rolled a {player1_score}")
    print(f"{player2} rolled a {player2_score}")

    if player1_score > player2_score:
        print(f"{player1} wins!")  
    elif player2_score > player1_score:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")

main()