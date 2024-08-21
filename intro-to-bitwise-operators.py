#1/14
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#2/14
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

#3/14
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#4/14
print bin(1)

num_a = 2 
while num_a < 6:
  print bin(num_a)
  num_a += 1 

num_b = 1
for i in range(5):
  print bin(num_b)
  num_b += 1

#5/14
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int('11001001', 2)

#6/14
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2 # output: 3
shift_left = shift_left << 2 # output: 4

print bin(shift_right)
print int('0b11', 2)
print bin(shift_left)
print int('0b100', 2)

#7/14
print bin(0b1110 & 0b101)

#8/14
print bin(0b1110 | 0b101)

#9/14
print '0b1011'
print bin(0b1110 ^ 0b101)

#10/14
print ~1
print ~2
print ~3
print ~42
print ~123

#11/14
def check_bit4(input):
  num = input
  mask = 0b01000
  desired = num & mask
  if desired > 0:
    return 'on'
  else: return 'off'

print check_bit4(0b1000)

#12/14
a = 0b10111011
mask = 0b100
desired = a | mask

print bin(desired)

#13/14
a = 0b11101110
mask = 0b11111111
desired = a ^ mask

print bin(desired)

#14/14
def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)