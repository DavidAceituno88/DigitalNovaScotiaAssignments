
import random 

roll = random.randint(1,6)

print("The computer rolled a: " + str(roll))

guess = int(input("Guess the number the dice roll:\n"))

if guess == roll :
    print("You won the dice roll was : " + str(roll))
else :
    print("Wrong the dice roll was: " + str(roll))
