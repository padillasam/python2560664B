import modulo1
#import modulo1 as m
#from modulo1 import suml,prodl
#from modulo1 import *
x=[2,2,2,2,2]
y=[3,3,3,3,3]

print(modulo1.suml(x))
print(modulo1.prodl(y))

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo1.suml(zeroes))
print(modulo1.prodl(ones))

import sys

for p in sys.path:
    print(p)