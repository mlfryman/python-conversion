from pip.backwardcompat import raw_input

age = 20
gender = 'female'

if age >= 21 and (gender == 'female' or gender == 'male'):
   print('go have a drink')
else:
   print('go have your parents buy you a drink')

for x in range(20, -50, -5):
   print("{0} to the {1} power is {2}".format(x, 2, x**2))

evens = [(x, x**2, y, y**3, x*y) for x in range(0, 20, 2) for y in range(3, 15, 3) if x == 10]

def sum(a,b):
    return a + b

a = sum(3,4)

# can import select vars from library: from math import pi; from math import * (brings in all)
# this is not suggested; it is called polluting your namespace.  restricts available var names
import math
def volume(height, radius):
    return math.pi * (radius**2) * height

b = volume(5, 10)

#Binary to Decimal Conversion
def bin2dec(bin):
    sum = 0
    for index, bit in enumerate(bin[::-1]):
        sum += int(bit) * (2**index)
    return sum

dec = bin2dec('10001')
print(dec)

#Binary to Decimal Conversion
def bin2dec(bin, base):
    """
    :param bin: binary string
    :param base: base
    :return: returns the binary string in decimal form
    """
    return int(bin, base) # Convert a binary string to a decimal int.
print('Decimal #: ', (bin2dec('1001', 2)))




#Decimal to Binary Conversion


a = 4


