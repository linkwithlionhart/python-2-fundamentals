"""
Welcome! This program is gonna be a banger of a classic that we all know: Rock, Paper, Scissors.

This program does the following:
  1. Prompt the user to select either Rock, Paper, or Scissors.
  2. Instruct the computer to randomly select either Rock, Paper, or Scissors.
  3. Compare the user's choice and the computer's choice.
  4. Determine a winner (the user or the computer).
  5. Inform the user who the winner is.
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Your opponent selected : %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else: 
    print message["lost"]
  
def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = str(raw_input("Enter Rock, Paper, or Scissors: "))
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()


  