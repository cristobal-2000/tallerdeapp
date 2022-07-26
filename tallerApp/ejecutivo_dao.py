from conexion import Conexion
from beautifultable import BeautifulTable


class Ejecutivo_dao:
    def __init__(self) -> None:
        pass
    def obtenerTique(self,ID) -> None:
        Conexion.cursor.execute("""SELECT * FROM TIQUE WHERE ID=:1""",[ID])    
        i = Conexion.cursor.fetchone()
        if i is None:
            return None
        else:
            return (i[0],i[1],i[2],i[3],i[4])
    def insertarDatos(self,t):
        Conexion.cursor.execute("""INSERT INTO TIQUES VALUES (:1,:2,:3,:4,:5)""",
        [t.ID,t.Nombre,t.correo,t.contraseña])
        Conexion.cursor.execute()
        return "se a insertado los datos"
    
    def EliminarDatos(self,ID):
        Conexion.cursor.execute("""DELETE FROM TIQUE WHERE ID_TIQUES=:1 """,[ID]) 
        Conexion.connection.commit()   