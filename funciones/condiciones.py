import random
def ascendente(x,y):
    if x<y:
        return 'Ascendente'
    elif x>y:
        return 'Descendente'
    else:
        return 'Iguales'
print(ascendente(1,5))
print(ascendente(10,5))
print(ascendente(10,10))
for i in range(10):
    x=round(random.randrange(100))
    y=round(random.randrange(100))
    print(x,' ',y,ascendente(x,y))
    