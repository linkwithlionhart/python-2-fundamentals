"""
The goal of this program is to build a calculator than coverts RGB value to hex values, vice-versa.

Three methods are involved:
- A method to convert RGB to Hex
- A method to convert Hex to RGB
- A method that starts the prompt cycle

The program does the following:
1. Prompt the user for the type of conversion they want
2. Ask the user to input the RGB or Hex value
3. Use Bitwise operators and shifting in order to convert the value
4. Print the converted value to the user
"""
def rgb_hex():
  invalid_msg = 'Input is invalid. Value must be between 0 and 255.'
  red = int(raw_input('Enter a red (R) value: '))
  green = int(raw_input('Enter a green (G) value: '))
  blue = int(raw_input('Enter a blue (B) value: '))
  RGB = [red, green, blue]
  for color in RGB:  
    if color < 0 or color > 255:
      print invalid_msg
      return
  val = (red << 16) + (green << 8) + blue
  print "%s" % hex(val)[2:].upper()

# rgb_hex()

def hex_rgb():
  invalid_msg = 'Invalid hexidecimal value. Try again.'
  hex_val = raw_input('Enter a six-digit hexidecimal value: ')
  
  if len(hex_val) != 6:
    print invalid_msg
    return
  else: 
    hex_val = int(hex_val, 16)
    print 'Hex_val: %d' % hex_val
  
  # represents two hexadecimal digits
  two_hex_digits = 2**8
  
  # returns the first RGB value from right to left
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits

  # print the RGB values
  print 'RGB(%s, %s, %s)' % (red, green, blue)

# hex_rgb()

def convert():
  while True:
    option = raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ')

    if option == '1':
      print 'RGB to Hex...'
      rgb_hex()
    elif option == '2':
      print 'Hex to RGB...'
      hex_rgb()
    elif option == 'X' or option == 'x':
      break
    else: 
      print 'Error.'
  
convert()

