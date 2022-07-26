class Ejecutivo:
    def __init__(self, ID , Nombre, Contraseña, Correo) -> None:
        self.__ID = ID
        self.__Nombre = Nombre
        self.__Contraseña = Contraseña
        self.__Correo = Correo
 
    @property
    def ID_tiques(self):
        return self.__ID 

    @property
    def Nombre(self):
        return self.__Nombre


    @property
    def Fecha(self):
        return self.__Contraseña     

    @property
    def Correo(self):
        return self.__Correo

