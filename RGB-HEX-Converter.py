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
  val = (red << 16) + (green << 8) + blue
  print "%s" % hex(val)[2:].upper()

rgb_hex()

