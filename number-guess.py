"""
In this progam, the user rolls a pair of dice and guess the sum. If the user's guess is equal to the to total value of the dice roll, the user wins.

The program does the following: 
  1. Roll a pair of dice.
  2. Add the values of the roll.
  3. Ask the user to guess a number.
  4. Compare the user's guess to the total value.
  5. Determine the winner (user or computer).
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Predict the sum of two dice. What's your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(2, number_of_sides)
  max_val = number_of_sides * 2
  print "The highest sum you may guess is %d." % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "Your guess is larger than the max value!"
    print "Try again."
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    total_roll = first_roll + second_roll
    print "The total value is: %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Congratulations, you beat the odds. You got it right!"
    else: 
      print "Nice try, but the odds were against you. Try again!"


roll_dice(6)