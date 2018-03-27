# This script is all about Bitwise operators

# Bitwise operators in an example
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR -> Note that XOR-ing a number with itself will always result in 0
# a = 0b11101110
#
# mask = 0b11111111
# desired = a ^ mask
#
# print bin(desired)
print ~88     # Bitwise NOT -> Flips all bits in a single bin- number.
# mathematically, this is equivalent to adding one to the number and then making it negative

Writing in Binary format:
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

# Functions to change inbetween bases bin(), oct() and hex()
print int("11001001",2)

# Left Bit Shift (<<)
#0b000001 << 2 == 0b000100 (1 << 2 = 4)
#0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
#0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
#0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

# Bit Mask operations
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"

def check_bit4(input):
  if (input & 0b1000) == 0b1000:
    return "on"
  else:
    return "off"

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)
