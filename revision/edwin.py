class Persona:#se llama la clase y se le coloca 
    def __init__(self,nombre,documento): #con esta funcion se inicializa el constructor
        self.__nombre=nombre
        print('Activando constructor')#este print indica que ya inicia a correr el constructor
        self.__documento=documento
       
    def getNombre(self):#con getter podemos acceder al valor 
        return self.__nombre  #con el return tomamos los valores 
    
    def setNombre(self, nombre):
        self.__nombre=nombre#con self podemos vincular los atributos    
    
    
    def setdocumento():#con setter podemos cambiar el valor
        self.__documento=documento
        
    def getdocumento(self):
        return self.__documento#en esta linea le indicamos al 
    
    
    
    def metodo(self):
        print('Soy un método')


ob=Persona('Ana','100048495')
print(ob.getNombre())#con este print mostramos en pantalla los
ob.setNombre('Maria')#este metodo cambia el nombre en este caso cambiaria Ana por Maria
#ob.getdocumento
#ob.setdocumento
print(ob.getNombre())
print(ob.getdocumento())