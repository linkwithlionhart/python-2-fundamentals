#1/18
my_dict = {
  'name': 'Will',
  'age': 32,
  "DTF": False
}

print my_dict.items()

#2/18
print my_dict.keys()
print my_dict.values()

#3/18
for key in my_dict:
  print key, my_dict[key]

#4/18 - list comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#5/15
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if (x ** 2) % 2 == 0]

print even_squares

#6/15
