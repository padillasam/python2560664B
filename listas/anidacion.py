import random
filas=round(random.randint(2,5))
lista=[[] for i in range(filas) ]
print(lista)
col=round(random.randint(2,5))
"""
for i in lista:
    for j in range(col):
        i.append(round(random.random()*100))
print(lista)
"""
lista1=[[round(random.random()*100) for i in range(col)] for i in range(filas)]
print(lista1)
"""
listaAnidada=[[1,2,3],
              [4,5,6],
              [7,8,9]]
lista1=[]
for i in range(5):
    lista1.append([])
print(lista1)

lista2=[[] for i in range(10)]

lista2[0].append(100)
print(lista2)

"""