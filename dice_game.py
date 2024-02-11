import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Type Player 1 Name: ")
    player2 = input("Type Player 2 Name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    if roll1 > roll2 :
        print(f"{player1} won! he rolled {roll1} and {player2} rolled {roll2}")
    elif roll1 < roll2 :
        print(f"{player2} won! he rolled {roll2} and {player1} rolled {roll1}")
    else :
        print(f"DRAW! {player1} rolled {roll1} and {player2} rolled {roll2}")

main()
