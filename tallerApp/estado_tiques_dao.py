from conexion import Conexion
from beautifultable import Beautifultable
from estado_tiques_dao import estado_tiques

class Tique_dao:
    def __init__(self) -> None:
        pass
    def obtenerTique(self,ID_tiques) -> None:
        Conexion.cursor.execute("""SELECT * FROM TIQUE WHERE ID_TIQUES=:1""",[ID_tiques])    
        i = Conexion.cursor.fetchone()
        if i is None:
            return None
        else:
            return (i[0],i[1],i[2],i[3],i[4])
    def insertarDatos(self,t):
        Conexion.cursor.execute("""INSERT INTO TIQUES VALUES (:1,:2,:3,:4,:5)""",
        [t.ID_tiques,t.Nombre,t.Estado])
        Conexion.cursor.execute()
        return "se a insertado los datos"
    
    def EliminarDatos(self,ID_tiques):
        Conexion.cursor.execute("""DELETE FROM TIQUE WHERE ID_TIQUES=:1 """,[ID_tiques]) 
        Conexion.connection.commit()   
        return "se a eliminado los datos"
