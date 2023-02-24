import sys
from sys import path
#path.append('C:\\Users\\usuario\\Dropbox\\sena2022\\Trimestre4-06octubre-17diciembre\\MiPracticaPythonB\\modulos')
path.append('..\\MiPracticaPythonB\\modulos')

# for p in sys.path:
#     print(p)
#path.append('..\\modules')
import modulo1

x=[1,1,1,1,1]
y=[2,2,2,2,2]
print('--------')
print(modulo1.__counter)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo1.suml(zeroes))
print(modulo1.prodl(ones))
print(modulo1.suml(zeroes))
print(modulo1.prodl(ones))
print(modulo1.suml(x))
print(modulo1.prodl(y))

print(modulo1.__counter)

