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

#5/18
  doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
  even_squares = [x ** 2 for x in range(1, 12) if (x ** 2) % 2 == 0]

  print even_squares

#6/18
  cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
  print cubes_by_four

#7/18 - list slicing syntax
  l = [i ** 2 for i in range(1, 11)]
  # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

  print l[2:9:2]
  # Prints [9, 25, 49, 81]

#8/18
  my_list = range(1, 11) # List of numbers 1 - 10

  # Add your code below!
  print my_list[::2]

#9/18
