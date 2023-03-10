class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,titulo):
        self.__cursos.append(titulo)

    def getCursos(self):
        return self.__cursos

class Curso:
    def __init__(self,titulo):
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo
    
a=Aprendiz('Martha')
c1=Curso('Python Intermedio')
c2=Curso('Python Basico')
c3=Curso('Introduccion a Java')

a.agregarCurso(c1)
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos())


for curso in a.getCursos():
    print(curso.getTitulo())

del(a)
#print(a)
print(c1.getTitulo())