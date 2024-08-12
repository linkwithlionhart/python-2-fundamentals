"""
Loops
"""

# 1/19
  count = 0

  if count < 5:
    print "Hello, I am an if statement and count is", count

  while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

# 2/19
  loop_condition = True

  while loop_condition:
    print "I am a loop"
    loop_condition = False

  # 3/19
  num = 1

  while num < 11:  # Fill in the condition
    # Print num squared
    print num ** 2
    # Increment num (make sure to do this!)
    num += 1

# 4/19
  choice = raw_input('Enjoying the course? (y/n)')
  print choice
  print type(choice)

  while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

  """
  Lesson: using 'or' to join two boolean expressions will always return 'True'
  - if one is 'y' or if one is 'n', the result will be true
  - if both are 'y' or 'no', the result will be true
  """

# 5/19
  count = 0

  while count < 10: # Add a colon
    print count
    # Increment count
    count += 1

# 6/19
  count = 0

  while True:
    print count
    count += 1
    if count >= 10:
      break

# 7/19
  import random

  print "Lucky Numbers! 3 numbers will be generated."
  print "If one of them is a '5', you lose!"

  count = 0
  while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
      print "Sorry, you lose!"
      break
    count += 1
  else:
    print "You win!"

# 8/19
  from random import randint

  # Generates a number from 1 through 10 inclusive
  random_number = randint(1, 10)

  guesses_left = 3
  print guesses_left
  # Start your game!
  guess = int(raw_input("Your guess: "))
  guesses_left -= 1
  while guesses_left > 0:
    guesses_left -= 1
    if guess == random_number:
      print "You win!"
      break
    elif guess != random_number:
      print "Try again."
      guess = int(raw_input("Your guess: "))
  else:
    print "You lose."
  
  """
  Lesson: counters, increments, and decrements were tricky here. 
  - I set the guesses to end after 3 tries.
  - However, the loop was active until 4.
  - The issue is the raw_input guess before the while loop.
  - The guesses do not take that initial attempt as a try.
  - The fix was to immediately decrement the guesses after the raw_input.
  - The loop resolved after three attempts on the no-win path.
  """

# 9/19