from Vehiculo import *
class Carga(Vehiculo):
    def __init__(self,placa,conductor,capacidad,ejes):
        Vehiculo.__init__(self,placa,conductor)
        self.__capacidad=capacidad
        self.__ejes=ejes    
    def getCapacidad(self):
        return self.__capacidad    
    def getEjes(self):
        return self.__ejes