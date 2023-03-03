class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getDocumento(self):
        return self.__documento
    
    def setDocumento(self,documento):
        self.__documento=documento

ob=Persona('Ivan',1030533045)
print(ob.getNombre(),ob.getDocumento())
ob.setNombre('Goku')
ob.setDocumento(1045534768)
print(ob.getNombre(),ob.getDocumento())