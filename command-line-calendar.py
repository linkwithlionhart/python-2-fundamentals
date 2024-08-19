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
        break
      else: 
        print calendar
        break
    elif user_choice == 'U':
      date = raw_input('What date? ')
      update = raw_input('Enter the update: ')



start_calendar()



