var=1
while var!='6':
    print('1-Ingresar cancion')
    print('2-Ingresar artista')
    print('3-ver lista de canciones')
    print('4-ver cancion mas larga')
    print('5-ver cancion mas corta')
    print('6-salir')
    #var=int(input('ingrese estrato'))
    var=input('ingrese estrato')
    match var:
        case '1':
            print('descuento 50%')        
        case '2':
            print('descuento 40%')
        case '3':
            print('descuento 30%')
        case _:
            print('No hay descuento')
print('FIN')
# if var=='1':
#     print('descuento 50%')
# elif var =='2':
#     print('descuento 40%')
# elif var=='3':
#     print('descuento 30%')
# else:
#     print('no hay descuento')