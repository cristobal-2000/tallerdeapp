"""una clase que se creo para iniciar cada variable y sus property """
class Tique:
    def __init__(self, ID_tique , Nombre, Estado,) -> None:
        self.__ID_tique = ID_tique
        self.__Nombre = Nombre
        self.__Estado = Estado

    @property
    def ID_tique(self):
        return self.__ID_tique 

    @property
    def Nombre(self):
        return self.__Nombre


    @property
    def Estado(self):
        return self.__Estado      

