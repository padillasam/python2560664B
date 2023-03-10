class Curso:
    def __init__(self,titulo):
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo

class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,nombreCursito):
        cursito=Curso(nombreCursito)
        self.__cursos.append(cursito)

    def getCursos(self):
        return self.__cursos
    
ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())

del ap
print(ap)

