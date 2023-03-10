# x=int(input('ingrese valor'))
# print('salidas a consola')
flujo=open('archivos/basico.txt','r')
#datos=flujo.read()
#print(type(datos))
#flujo.write('Bienvenido al trabajo con archivos')
for dia in flujo:
    print(dia)
#flujo.close()

with open ('archivos/basico.txt','r') as flujo:
    datos=flujo.read()
    print(datos)

with open ('archivos/basico.txt','r') as flujo:
    for dia in flujo:
        print(dia)
