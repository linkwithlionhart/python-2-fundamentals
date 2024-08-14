"""
Here we've created a simple calculator that can compute the area of circles and triangles. 

The program can do the following:
1. Prompt the user to select a shape.
2. Calculate the area of that shape.
3. Print the area of that shape to the user.
"""

print "Loading calculator..."
name = raw_input("What's your name? ")
option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter a value for the radius: "))
  pi = 3.14159
  area_c = pi * radius**2
  print "%s, with a radius of %s, the area of the cirle is %s" % (name, radius, area_c)
elif option == "T":
  base = float(raw_input("Enter a value for the base: "))
  height = float(raw_input("Enter a value for the height: "))
  t_area = 0.5 * base * height
  # Or t_area = 1.0/2 * base * height
  print "%s, with a base and height of %s and %s, the area of the triangle is %s" % (name, base, height, t_area)
else: 
  print "Sorry, you did not enter the required input."
  print "Please reboot the application."

print "Thank you for using our simple Area Calculator."

"""
Lesson learned: in Python, dividing an integer by an integer produces an integer.
In my attempt to make a half-value, I typed '1/2' multiplied by the base and height. 
The area returned is 0.0. The fix was using a float point value of 0.5.
"""