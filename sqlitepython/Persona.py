class Persona:    
    
    def __init__(self,id,nombre,apellido,email):
        self.__id=id
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombreCompleto(self):
        return self.__nombre+' '+self.__apellido
