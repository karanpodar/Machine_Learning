# Rock Paper & Scissors Game
import random

computer = random.choice(["Scissors","Rock","Paper"])

user = input("Do you want Rock, Paper or Scissors?\n")

print ("Computer's choice " + computer)

if computer == user:
    print ("TIE")
elif computer == "Scissors" and user == "Rock":
    print ("You win")
elif computer == "Scissors" and user == "Paper":
    print ("You lose")
elif computer == "Rock" and user == "Scissors":
    print ("You lose")
elif computer == "Rock" and user == "Paper":
    print ("You Win")
elif computer == "Paper" and user == "Scissors":
    print ("You Win")
elif computer == "Paper" and user == "Rock":
    print ("You lose")
else:
    print("Enter valid value")
    
    
