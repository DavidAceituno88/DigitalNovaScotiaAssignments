import random
computer_choice = random.choice(['rock','paper','scissors'])
user_choice = input("Do you want rock, paper or scissors? :")

if (computer_choice == user_choice):
    print('TIE')
    print("Computer's choice = " + computer_choice)  
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You won!") 
    print("Computer's choice = " + computer_choice)  
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You won!")
    print("Computer's choice = " + computer_choice)  
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You won!")
    print("Computer's choice = " + computer_choice)  
else :
    print("You lose")
    print("Computer's choice = " + computer_choice)  
