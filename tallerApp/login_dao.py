from sqlite3 import Row
from conexion import Conexion
import os


class Login_dao:
    def __init__(self) -> None:
        pass

    def validacion(self,userValidacion,contrasena):
        Conexion.cursor.execute(
            """SELECT  ID_USUARIO FROM LOGIN""")
        usuariosbbdd = Conexion.cursor.fetchall()
        Conexion.cursor.execute(
            """SELECT  CONTRASENA FROM LOGIN""")
        contrasenaUser = Conexion.cursor.fetchall()
        
        for i in usuariosbbdd:
            user= i[0]
            if user == userValidacion:
                indice = usuariosbbdd.index(i)
                cosa = contrasenaUser[indice]
                clave = cosa[0]

                if clave == contrasena:
                    os.system('cls')
                    print('-----------CREDENCIALES CORRECTAS-------------')
                    return True
        
        return False

        


