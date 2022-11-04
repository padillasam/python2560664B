import random
vec=[]
for i in range (30):
    vec.append(round(random.randint(5,28)))
print(vec)
m1=vec[:15]
s=0
for i in m1:
    s+=i
print('Promedio primera quincena=',s/len(m1))
m2=vec[15:-1]
t1=vec[:11]
print(m1)
print(m2)
print(t1)