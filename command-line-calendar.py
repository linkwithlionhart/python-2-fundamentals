"""
The goal of this program is to build a basic calendar that the user can interact with from the command line. The user is able to do the following:
  View the calendar
  Add an event to the calendar
  Update an existing event
  Delete an existing event

The program is expected to behave in the following way:
  1. Print a welcome message to the user.
  2. Prompt the user to view, add, update, or delete an event on the calendar.
  3. Depending on the user's input: view, add, update, or delete an event on the calendar.
  4. The program should never terminate unless the user decides to exit.
"""

from time import sleep, strftime

user = 'William'
calendar = {

}

def welcome():
  print 'Welcome, %s.' % user
  print 'Your calendar is booting...'
  sleep(1)
  print 'Today is ' + strftime("%A, %B %d, %Y")
  print 'The current time is ' + strftime('%H:%M:%S')
  sleep(1)
  print 'What would you like to do?'

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input('Choose from the following options. A to Add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else: 
        print calendar
    elif user_choice == 'U':
      date = raw_input('What date? ')
      update = raw_input('Enter the update: ')
      # dangerous: does not run any validations for the update
      calendar[date] = update
      print 'Update complete.'
      print calendar
    elif user_choice == 'A':
      event = raw_input('Enter event: ')
      date = raw_input('Enter date (MM/DD/YYYY): ')
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print 'Invalid date entered.'
        try_again = raw_input('Try again? Y for Yes, N for No: ')
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else: 
        calendar[date] = event
        print 'Date successfully added.'
        print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1: 
        print 'Your calendar is empty.'
      else:
        event = raw_input('What event? ')
      for date in calendar.keys():
        if event == calendar[date]:
          del calendar[date]
          print 'Deletion successful.'
          print calendar
        else: 
          print 'Invalid date entered.'
    elif user_choice == 'X':
      print 'See you later.'
      start = False
    else:
      print 'Invalid command.'
      start = False

start_calendar()