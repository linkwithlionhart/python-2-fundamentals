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
class Car(object):
  condition = 'new'

  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car = Car('DeLorean', 'silver', 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg

"""
Lesson: We use dot notation to access the values of member variables of classes because those variables belong to the object. 
"""

#7/11 - creating class methods
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  
  def display_car(self):
    print 'This is a %s %s with %s MPG.' % (self.color, self.model, str(self.mpg))

my_car = Car("DeLorean", "silver", 88)
my_car.display_car()

"""
Lesson: need to provide 'self' as the first argument of any class method.
"""

#8/11 - modifying member variables
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

#9/11 - inheritance from parent classes to child classes
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.battery_type
print my_car.model

#10/11 - overriding methods
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
  
  def drive_car(self):
    self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

#11/11 - building useful classes
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2 , 3)
print my_point

