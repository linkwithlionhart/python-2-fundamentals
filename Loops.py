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
  print "Counting..."

  for i in range(20):
    print i  

# 10/19
  hobbies = []

  # Add your code below!
  for hobby in range(3):
    hobby = str(raw_input("What is your hobby? "))
    hobbies.append(hobby)
    print hobbies

# 11/19
  thing = "spam!"

  for c in thing:
    print c

  word = "eggs!"

  # Your code here!
  for letter in word:
    print letter

# 12/19
  phrase = "A bird in the hand..."

  # Add your for loop
  for char in phrase:
    if char == "A" or char == "a":
      print "X",
    else:
      print char,

  #Don't delete this print statement!
  print

# 13/19
  numbers  = [7, 9, 12, 54, 99]

  print "This list contains: "

  for num in numbers:
    print num

  # Add your loop below!
  for num in numbers:
    print num ** 2

# 14/19
  d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

  for key in d:
    # Your code here!
    print key + " " + d[key]
  
# 15/19
  choices = ['pizza', 'pasta', 'salad', 'nachos']

  print 'Your choices are:'
  for index, item in enumerate(choices):
    print index+1, item

# 16/19
  list_a = [3, 9, 17, 15, 19]
  list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

  for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
      print a
    else:
      print b
    # print a, b
    # print zip(list_a, list_b)

  for a,b in zip(list_a, list_b):
    print max(a, b)

# 17/19
  fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

  print 'You have...'
  for f in fruits:
    if f == 'tomato':
      print 'A tomato is not a fruit!' # (It actually is.)
      break
    print 'A', f
  else:
    print 'A fine selection of fruits!'
  
  """
  In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. 
  This code will break when it hits 'tomato', so the else block won’t be executed.
  """

# 18/19
  fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

  print 'You have...'
  for f in fruits:
    if f == 'tomato':
      print 'A tomato is not a fruit!' # (It actually is.)
      # break
    print 'A', f
  else:
    print 'A fine selection of fruits!'

# 19/19
  from random import randint

  starters = [
    'Squirtle', 'Charmander', 'Bulbasaur', 'Pikachu', 'Eevee'
    ]

  def select(starters):
    randomizer = random.randint(0, 8)
    if randomizer <= 4:
      selection = starters[randomizer]
      return selection

  # print 'User has chosen: ' + select(starters)

  for pokemon in starters:
    if select(starters) == pokemon:
      print 'With, ' + pokemon + '. You may become champion.'
      break
    print pokemon
  else: 
    print 'You will not become champion.'