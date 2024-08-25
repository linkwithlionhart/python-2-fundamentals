"""
This program contains a class which creates and manipulates a personal bank account.

The bank account class does the following:
- Accepting deposits
- Allowing withdrawals
- Showing the balance
- Showing the details of the account
"""

class BankAccount(object):
  balance = 0

  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return 'Name: %s, Balance: $%.2f' % (self.name, self.balance)
  
  def show_balance(self):
    print 'Balance: $%.2f' % self.balance

  def deposit(self, amount):
    if amount <= 0:
      print 'Sorry, you must deposit more than zero dollars.'
      return
    else: 
      self.balance += amount
      print 'Amount deposited: $%.2f' % amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print 'Sorry, your withdrawl must not exceed your balance.'
      return
    else:
      self.balance -= amount
      print 'Amount withdrawn: $%.2f' % amount
      self.show_balance()

my_account = BankAccount('Will')
print my_account.name
print my_account.balance
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account