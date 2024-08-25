#1/9
  my_list = [i ** 2 for i in range(1, 11)]
  # Generates a list of squares of the numbers 1 - 10

  f = open("output.txt", "w")

  for item in my_list:
    f.write(str(item) + "\n")

  f.close()

#2/9 open() function
  # enable read and write to file
  my_file = open('output.txt', 'r+')

#3/9 writing
  my_list = [i ** 2 for i in range(1, 11)]
  print my_list

  my_file = open("output.txt", "w")
  print type(my_file)

  # Add your code below!
  for item in my_list:
    my_file.write(str(item) + '\n')

  print my_file
  my_file.close()
  print my_file

#4/9 reading
  # issue a command to read with open() and 'r'
  my_file = open('output.txt', 'r')
  print my_file.rea

  # always close your file
  my_file.close()
  print my_file

#5/9 reading between the lines
  my_file = open('text.txt', 'r')

  print my_file.readline()
  print my_file.readline()
  print my_file.readline()

  # never forget to close
  my_file.close()

#6/9 PSA: buffering data
  # Use a file handler to open a file for writing
  write_file = open("text.txt", "w")

  # Open the file for reading
  read_file = open("text.txt", "r")

  # Write to the file
  write_file.write("Not closing files is VERY BAD.")
  write_file.close()

  # Try to read from the file
  print read_file.read()
  read_file.close()

  """
  Lesson: Always close the file, otherwise Python will not flush/write the data to the file. It is setup to write to the file once you ensure the file is closed. If not, the data will not be saved.
  The implication here is that you will know if a file is successfully closed if the written data is viewable.
  """

#7/9 - 'with' and 'as' keywords
  with open("text.txt", "w") as textfile:
    textfile.write("Success!")

  """
  Lesson: file objects contain special built in methods to enter and exit. They are invoked with two key-word pairs: 'with' and 'as'.
  The code segment works as if the file was explicitly closed. The text is successfully written to the file.
  """

#8/9 DIY
  with open('text.txt', 'w') as my_file:
    my_file.write('Does this work?')

#9/9 case closed?
  with open('text.txt', 'w') as my_file:
    print my_file.closed
    my_file.write('Does this work?')
    if my_file.closed == False:
      my_file.close()
    print my_file.closed

  """
  Lesson: file object come with an attribute called 'closed' and returns a Boolean value. We can use this object attribute to check it's status.
  """