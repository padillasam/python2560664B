class Conductor:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
        