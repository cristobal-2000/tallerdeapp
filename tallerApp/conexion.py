import cx_Oracle

class Conexion:
    connection=None
    cursor=None

    @classmethod
    def getStartConnection(cls):
        #este ruta es la del ORACLE CLIENT
       cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_3")
       if cls.connection is None:
        connect = cx_Oracle.connect(user="CRISTOBAL", password="TallerSistemas2022", dsn="tallerdesarrollosistemasdiurno_high")
        cls.cursor = connect.cursor()
        cls.connection = connect
       

