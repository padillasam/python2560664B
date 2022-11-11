def saludo(nombre,programa):
    print('Hola ',nombre, 'ud estudia',programa)

def saludar(nombre, programa):
    return 'Hola ',nombre, 'ud estudia',programa

print(saludar('juan','animación'))
dato=saludar('juan','animación')
print(dato)
print(len(dato))


saludo('Ana','ADSO')
saludo('Gloria','contabilidad')

def parimpar(n):    
    print('Tipo de n')
    if n%2==0:
        print('par')        
    else:
        print('impar')

parimpar(1.5)

#return
