with open ('archivos/basico.txt','r') as flujo:
    datos=flujo.read()
    print(datos)

with open ('archivos/basico.txt','r') as flujo:
    for dia in flujo:
        print(dia)