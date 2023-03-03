class Persona:    
    nacionalidad='Colombia'
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        print('Activando constructor')

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    # def metodo(self,mail):
    #     self.__mail=mail
        #print('Soy un método')


ob=Persona('Ana',12345)
ob.mail='ana@mail.com'
print(ob.mail)
ob1=Persona('Luis',54321)
print(ob.nacionalidad)
print(ob1.nacionalidad)
print(Persona.nacionalidad)