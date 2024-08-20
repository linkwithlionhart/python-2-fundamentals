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
  my_list = range(1, 11)

  # Add your code below!
  backwards = my_list[::-1]
  print backwards

#10/18
  to_one_hundred = range(101)
  # Add your code below!
  backwards_by_tens = to_one_hundred[::-10]
  print backwards_by_tens

#11/18
  to_21  = range(1,22)
  print to_21

  odds = to_21[::2]
  print odds 

  middle_third = to_21[7:14:]
  print middle_third

#12/18 - anonymous functions
  my_list = range(16)
  print filter(lambda x: x % 3 == 0, my_list)

#13/18 - Lambda functions
  languages = ["HTML", "JavaScript", "Python", "Ruby"]

  # Add arguments to the filter()
  print filter(lambda x: x == "Python", languages)

#14/18
  squares = [x ** 2 for x in range(1,11)]
  print squares

  print filter(lambda x: x > 29 and x < 71, squares)

#15/18 - iterating over dictionaries
  movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

  print movies.items()
  print movies.keys()
  print movies.values()

#16/18
  threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

  print threes_and_fives

#17/18
  garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
  message = garbled[::-2]
  print message

#18/18
  garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
  message = filter(lambda x: x != 'X', garbled)
  print message