from Carga import *
from Conductor import *
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor')
docConductor=int(input('Ingrese documento del conductor'))
placa=input('ingrese placa')
capacidad=input('ingrese capacidad en toneladas')
ejes=input('ingrese numero de ejes')
c1=Conductor(nomConductor,docConductor)
obCarga=Carga(placa,c1,capacidad,ejes)
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())

with open('poo-archivos/listado.txt','a') as flujo:
    flujo.write(cadCarga+'\n')