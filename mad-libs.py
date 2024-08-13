"""
Mad Libs require:

A short story with blank spaces (asking for different types of words).
Words from the player to fill in those blanks.

1. Prompt the user for inputs.
2. Print the story with the inputs in the right places.

"""

"""
Description: This application is a word game that contains short stories with blank spaces a player can fill in. 
Author: WL
"""

"""
Description: This application is a word game that contains short stories with blank spaces a player can fill in. 
Author: WL
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print "Welcome, player. The game has begun."

name = raw_input("Enter a name: ")

print "Hello, %s." % (name)

adj_first = raw_input("Enter one adjective: ")
adj_second = raw_input("Enter second adjective: ")
adj_third = raw_input("Enter third adjective: ")
verb = raw_input("Enter a verb: ")
noun_first = raw_input("Enter a noun: ")
noun_second = raw_input("Enter another noun: ")

print "%s, you have provided the following adjectives %s, %s, %s." % (name, adj_first, adj_second, adj_third)

input_list = ['animal', 'food', 'fruit', 'superhero', 'country', 'dessert', 'year']
output_list = []

for each in input_list:
  get_each = raw_input("Enter a(n) %s: " % (each))
  output_list.append(get_each)

print output_list

# assign from array
animal = output_list[0]
food = output_list[1]
fruit = output_list[2]
superhero = output_list[3]
country = output_list[4]
dessert = output_list[5]
year = output_list[6]

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." % (name, adj_first, adj_second, animal, food, verb, noun_first, fruit, adj_third, name, superhero, name, country, name, dessert, name, year, noun_second)

print STORY





















