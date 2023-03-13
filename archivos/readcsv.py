from Aprendiz import *
import csv
listaAprendices=[]
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
#with open('files/people.csv') as csvDataFile:
#with open('https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html/addresses') as csvDataFile:
    csvReader=csv.reader(csvDataFile)
    #print(csvReader)
    for row in csvReader:
        apr=Aprendiz(row[0],row[1],row[2],row[3])
        listaAprendices.append(apr)
        #print(row)
        #print('first name:',row[0])
        #print('last name:',row[1])
        #print('email:',row[2])
        #print('id:',row[3])
print(listaAprendices)
for apr in listaAprendices:
    print(apr.nombreCompleto())