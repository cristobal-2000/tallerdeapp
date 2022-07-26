class Estado_Tique:
    def __init__(self, ID_tiques , Nombre, Estado  ) -> None:
        self.__ID_tiques = ID_tiques
        self.__Nombre = Nombre
        self.__Estado = Estado
        
 
    @property
    def ID_tiques(self):
        return self.__ID_tiques 

    @property
    def Nombre(self):
        return self.__Nombre


    @property
    def Estado(self):
        return self.__Estado      



