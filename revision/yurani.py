class Persona:   
    def __init__(self,nombre,documento): 
        self.__nombre=nombre                #constructor de clases
        self.__documento=documento

    def getNombre(self):                    #metodo
        return self.__nombre                #atributo
    
    def getDocumento(self):
        return self.__documento
        
    def setNombre(self, nombre):     
        self.__nombre=nombre   

    def setDocumento(self,documento):
        self.__documento=documento

                                            #objeto es el que inicia y recoge todos los metodos de una clase (persona)

ob=Persona('Ana',148523)   
print(ob.getNombre(),ob.getDocumento())   
ob.setNombre('tomsito')  
ob.setDocumento(10533045)
print(ob.getNombre(),ob.getDocumento())