# Rock Paper & Scissors Game
import random

computer = random.choice(["scissors","rock","paper"])

user = input("Do you want Rock, Paper or Scissors?\n").lower()

print ("Computer's choice " + computer, "\nYour Choice " + user)

if computer == user:
    print ("TIE")
elif user in ('rock', 'scissors', 'paper'):
    if (computer == "scissors" and user == "rock") | (computer == "rock" and user == "paper") | (computer == "paper" and user == "scissors"):
        print ("You win")
    else:
        print ("You Lose")
else:
    print("Enter valid value")