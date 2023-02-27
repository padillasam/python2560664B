class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        print('Activando constructor')

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def metodo(self):
        print('Soy un método')


ob=Persona('Ana')
print(ob.getNombre())
ob.setNombre('Maria')
print(ob.getNombre())
#ob.metodo()
#print(type(ob))