from itertools import product
import crcmod.predefined
from math import factorial
import string
 
# Init variables
found = False
currLen = 4
txtTarget = ""
crcTarget = 0
userDigit = "0001"

# Init functions
def crc(data):
        crcInstance = crcmod.predefined.Crc("crc-16")
        crcInstance.update(str(data).encode("utf-8", "replace"))
        return crcInstance.crcValue
 
def nCr(n,r):
    f = factorial
    return round(f(n) / f(r) / f(n-r))
 
# Get input
availableChars = string.ascii_letters + string.digits



#print ("CRC of target: " + hex(crcTarget))

while int(userDigit) < 10000:
	txtTarget = str("Agent Mona ID ") + str(userDigit)
	print txtTarget
	crcTarget = crc(txtTarget)
	print ("CRC of target: " + hex(crcTarget))
	userDigit = int(userDigit) + 1
