class Aprendiz:
    def __init__(self,fname,lname,email,id):
        self.__fname=fname
        self.__lname=lname
        self.__email=email
        self.__id=id

    def nombreCompleto(self):
        return self.__fname+' '+self.__lname
    