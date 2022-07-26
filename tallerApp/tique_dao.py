
from conexion import Conexion
from tique import Tique

#IMPORTAMOS TIQUE Y CONEXION , TIQUE PARA UTILIZARLO MEDIANTE FUNCION 


#una clase para distintas funciones del programa
#con un cursor hacemos una consulta sql para obtener los usuarios
#la funcion fetchall toda lo que obtuvimos con la consulta y lo pasa a una lista python

class Tique_dao:
    def __init__(self,) -> None:
        pass

    def buscarTique(self, ID_tique) -> Tique:
        """un conexion cursor para revisar la base de datos con una debida consulta"""
        Conexion.cursor.execute(
            """SELECT * FROM TIQUE WHERE ID_TIQUE=:1""", [ID_tique])
        Row = Conexion.cursor.fetchone()
        if Row is None:
            return None
        else:
            return Tique(Row[0], Row[1], Row[2],)

    def eliminarTique(self, ID_tique) -> str:
        if self.buscarTique(ID_tique) != None:
           Conexion.cursor.execute(
               """DELETE  FROM TIQUE WHERE ID_TIQUE=:1""", [ID_tique])
           Conexion.connection.commit()
           Conexion.cursor.execute("""DELETE FROM ESTADO_TIQUE WHERE ID_TIQUES=:1""",[ID_tique])
           Conexion.connection.commit()
           return 'ID ELIMINADO CORRECTAMENTE!'
        else:
            return 'ID no existe!'

    def insertarTique(self, Tique) -> str:
        if self.buscarTique(Tique.ID_tique) is None:
                Conexion.cursor.execute("""INSERT INTO ESTADO_TIQUE VALUES (:1,:2,:3)""", [
                                        Tique.ID_tique, Tique.Nombre, Tique.Estado])
                Conexion.connection.commit()
                Conexion.cursor.execute("""INSERT INTO TIQUE VALUES (:1,:2,:3)""", [
                                        Tique.ID_tique, Tique.Nombre, Tique.Estado])
                Conexion.connection.commit()
                return "se a insertado los datos"
        else:
            "no se han insertado los datos"

    def actualizarTique(self, v) -> str:
        if self.buscarTique(v.ID_tique) != None:
                print('los datos del ID son :', v.ID_tique, 'ID', v.Nombre, 'nombre', v.Estado, 'Estado')
                ID_ANTERIOR=v.ID_tique
                NOMBRE = input('indique un nombre:')
                ESTADO = input('indique el estado:')
                Conexion.cursor.execute("""UPDATE ESTADO_TIQUE SET NOMBRE=:1,ESTADO=:2 WHERE ID_TIQUES=:3""", [NOMBRE,ESTADO,ID_ANTERIOR])
                Conexion.connection.commit()
                Conexion.cursor.execute("""UPDATE TIQUE SET NOMBRE=:1,ESTADO=:2 WHERE ID_TIQUE=:3""", [NOMBRE,ESTADO,ID_ANTERIOR])
                Conexion.connection.commit()
                v = self.buscarTique(ID_ANTERIOR)
                print(v.ID_tique,v.Nombre,v.Estado)
                return "Tique actualizado correctamente"
        else:
            "no se a encontrado el tique" 
                                  

    
    


              
        
        

    
        