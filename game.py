#this is a rock paper scissors game!
import random

user_action = input("Enter a choice (rock, paper, scissors): ")
play = "rock", "paper", "scissors"
computer = random.choice(play)
print("\nYou chose",user_action,", computer chose",computer,".\n")

if user_action == computer:
  print("Both players selected", user_action,". It's a tie!")
elif user_action == "rock":
  if computer == "scissors":
    print("Rock beats scissors! You win!")
  else:
    print("Paper covers rock! You lose.")
elif user_action == "paper":
  if computer == "rock":
    print("Paper covers rock! You win!")
  else:
    print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
  if computer == "paper":
    print("Scissors cuts paper! You win!")
  else:
    print("Rock beats scissors! You lose.")
