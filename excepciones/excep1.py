#def divisores(num):
#     for i in range(num):
#         if num%i==0:
#             print(i,' es divisor')

# try:
#     divisores(19)
# except:

def divisores(num):

    if type(num)!=int:
        print('Solo trabaja con numeros')
    else:
        try:
            for i in range(1,num):
                if num%i==0:
                    print(i,' es divisor')
        except ZeroDivisionError:
            print('Indeterminacion')
        except TypeError:
            print('No ingreso un numero')
        except:
            print('Error no determinado')

divisores([])
print('El programa continua desde aqui')