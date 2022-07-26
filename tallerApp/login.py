



from login_dao import Login_dao


class Login:
    def __init__(self,id_usuario,contrasena,) -> None:
        self._id_usuario =id_usuario
        self._contrasena = contrasena
        



    @property
    def id_usuario(self):  
        return self.__id_usuario    

    @property
    def contrasena(self):
        return self.__contrasena   

      

    def validaciones(self):
        Validacion = Login_dao()
        if Validacion.validacion(self._id_usuario,self._contrasena)==True:
            return True
        else:
            return False
        
        

