anidado={
    'documento':123,
    'nombre':{
        'elnombre':'pablo',
        'apellido':'marmol',    
    },
    'programa':'adso',
    'cursos':['python','js','java']
}

print(anidado['documento'])
print(anidado['nombre']['apellido'])
#print(anidado['cursos'][0])
for i in anidado['cursos']:
    print(i)
#print(anidado.items())

