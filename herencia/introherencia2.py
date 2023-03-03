class A1:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A1')

class A2:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A2')


class B(A2,A1):
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):
        return 'Soy un objeto de la clase B'
obj=B()
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())