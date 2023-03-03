class Persona: #Esta linea define una clase llamada Persona.
    def __init__(self,nombre): #Esta línea define el método __init__, que es el constructor de la clase Persona. El constructor se llama automáticamente cuando se crea una instancia de la clase. El constructor toma como parámetros el objeto self (que se refiere a la propia instancia) y el argumento nombre.
        self.__nombre=nombre #En el cuerpo del constructor, se inicializa el atributo privado __nombre con el valor del parámetro nombre
        print('Activando constructor') #Esta linea imprime el mensaje 'Activando constructor'.

    def getNombre(self): #Esta línea define el método 'getNombre'.
        return self.__nombre #Devuelve el valor del atributo privado '__nombre' de la instancia.
    
    def setNombre(self, nombre): #Esta línea define el método setNombre.
        self.__nombre=nombre #Esta linea ctualiza el valor del atributo privado __nombre de la instancia con el valor del parámetro nombre.

    def metodo(self): #Esta línea define un método llamado metodo.
        print('Soy un método') #Esta line mprime el mensaje "Soy un método".


ob=Persona('Ana') #Esta línea crea una nueva instancia de la clase Persona y la asigna a la variable ob. El constructor de la clase se llama automáticamente con el argumento 'Ana'.
print(ob.getNombre()) #Esta línea llama al método getNombre de la instancia ob y muestra el valor del atributo privado __nombre.
ob.setNombre('Maria') #Esta línea llama al método setNombre de la instancia ob y actualiza el valor del atributo privado __nombre con el valor 'Maria'.
print(ob.getNombre()) #Esta línea llama de nuevo al método getNombre de la instancia ob y muestra el nuevo valor del atributo privado __nombre. En este caso, el resultado será 'Maria'.
#ob.metodo() #Imprime una cadena de caracteres en la consola: "Soy un método".
#print(type(ob)) #Muestra el tipo de objeto que es la variable 'ob'.