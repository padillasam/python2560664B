def sumaDivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma

def perfectos(num):
    sum=sumaDivisores(num)
    if sum==num:
        return 'perfecto'
    else:
        return 'No es perfecto'

print(perfectos(20))

def primos(num):
    sum=sumaDivisores(num)
    if sum==1:
        return 'Es primo'
    else:
        return 'No es primo'

print(primos(12))