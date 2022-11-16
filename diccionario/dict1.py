persona1={
    'nombre':{
        'primerNombre':'Ana',
        'segundoNombre':'Mejia'
    },
    'documento':12345,
}
persona2={
    0:'Maria Sharapova',
    1:54321,
}
persona2['edad']=20
persona2[0]='Mary'
print(persona2)
persona2.update({'telefono':102030})
print(persona2)
#print(persona2[0])
for item in persona2:
    print(item) 

for key in persona2.keys():
    print(key,'-> ',persona2[key])

for key, value in persona2.items():
    print("Clave ->", key, ":", value)
