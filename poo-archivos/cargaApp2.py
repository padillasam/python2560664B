from Conductor import *
from Carga import *
lista=[]
with open('poo-archivos/listado.txt','r') as flujo:
    for ob in flujo:
        lista.append(ob)
i=0
for ob in lista:
    lista[i]=ob.rstrip()
    i+=1
print(lista)
#placa, nombre,doc, cap, ejes
lautos=[]
for ob in lista:
    #for x in ob.split(','):
    lautos.append(ob.split(','))
cargas=[]
print(lautos)
for i in range(len(lautos)):
    #print(lautos[i][0])    
    p=lautos[i][0]
    n=lautos[i][1]
    d=lautos[i][2]
    c=lautos[i][3]
    e=lautos[i][4]
    con=Conductor(n,d)
    obj=Carga(p,con,c,e)
    cargas.append(obj)

print(cargas)    
# 
# for ob in lautos:
    
#     #for x in ob:
#      #   print(x)
#         # p=x[0]
#         # n=x[1]
#         # d=x[2]
#         # c=x[3]
#         # e=x[4]
#         # con=Conductor(n,d)
#         # obj=Carga(p,con,c,e)
#         # cargas.append(obj)
# print(cargas)