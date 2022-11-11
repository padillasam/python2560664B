import random
def llenarLista(list):
    tam=round(random.randint(5,20))
    for i in range(tam):
        list.append(round(random.randrange(100)))
    return list

def sumarLista(list):
    sum=0
    for i in list:
        sum+=i
    return sum

lista=[]
lista=llenarLista(lista)
print(lista)
print('La suma es=',sumarLista(lista))