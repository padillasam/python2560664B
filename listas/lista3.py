import random
tam=20
vec=[10,2,3,4,10,23,34,10,2,5]
vecCant=[]
#for i in range(tam):
 #   vec.append(round(random.random()*100))
print(vec)
cont=0
for i in range(len(vec)): 
    cont=0
    for j in vec:    
        if vec[i] == j:
            cont+=1 
    if cont!=0:
        vecCant.append(cont)
    else:
        vecCant.append(0)
print(vec)
print(vecCant)
mayor=0
pos=0
for i in range(len(vec)):
    if mayor<vecCant[i]:
       mayor=vecCant[i]
print('El mayor es ',mayor)
for j in range(len(vecCant)):
    if mayor==vecCant[j]:
        print('la moda es ',vec[j])