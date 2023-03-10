class Vehiculo:
    def __init__(self,placa,conductor):
        self.__placa=placa
        self.__conductor=conductor
    def getConductor(self):
        return self.__conductor
    def getPlaca(self):
        return self.__placa