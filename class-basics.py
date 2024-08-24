#1/11
class Car(object):
  pass

#2/11 0 - instance of a class
class Car(object):
  pass

my_car = Car()

#3/11 - class member variables
class Car(object):
  condition = 'new'

my_car = Car()

"""
Lesson: member variables are variables which belong to a class object.
"""

#4/11 - calling class member variables
class Car(object):
  condition = 'new'

my_car = Car()
print my_car.condition

#5/11 - initialize a class
class Car(object):
  condition = 'new'

  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car = Car('DeLorean', 'silver', 88)
print my_car.condition

#6/11 - refer to member variables

