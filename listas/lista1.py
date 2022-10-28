import random
tam=int(input('Ingrese cantidad'))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range(len(vec)):
    if vec[i]%2==0:
        print(vec[i],' par')
    else:
        print(vec[i],' impar')





"""
vector=[100,2,56,32,5,97,34,78]
print(len(vector))
#print(vector.__len__())
print(vector)
for i in range (len(vector)):
    print('posicion ',i,'valor ',vector[i])

for i in vector:
    print('valor ',i)

"""