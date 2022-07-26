from beautifultable import BeautifulTable
from conexion import Conexion
from login import Login
from tique import Tique
from tique_dao import Tique_dao
from estado_tiques import Estado_Tique
import time
import os
#importacion de archivos + un beautifultable para que de forma al menu + un import time para darle tiempo de respuesta
#me desvele estos dias para que funcionara
#me la quise jugar con una opcion de volver profe pero no me dio el tiempo 

os.system("cls") 
Conexion.getStartConnection()
tablaLogin = BeautifulTable()
tablaLogin.columns.header=["LOGIN"]
tablaLogin.rows.append([" Ingrese su Usuario y su Password"])
tablaLogin.rows.append([" Ingrese una x en el campo usuario para cerrar el programa"])
tablaLogin.columns.alignment = BeautifulTable.ALIGN_LEFT

def loginFuncion():
    os.system('cls')
    while True:
        
        print(tablaLogin)
        Usuario = input('Usuario: ')
        if Usuario=="x":
            break
        Password = input('Password: ')
        Datos = Login(Usuario,Password)
        if Datos.validaciones()==True:
            menuFuncion()
            break
        else:
            os.system('cls')
            print("-------CLAVES INCORRECTAS, INTENTE NUEVAMENTE---------")
            pass







menu = BeautifulTable()
menu.columns.header=["BIENVENIDO A CENTRO DE TIQUES"]
menu.rows.append(["1.= Buscar Tique"])
menu.rows.append(["2.= Eliminar Tique"])
menu.rows.append(["3.= Insertar Tique"])
menu.rows.append(["4.= Actualizar Tique"])
menu.rows.append(["5.= Cerrar Sesión"])
menu.rows.append(["6.= Salir del programa"])
"""menu para la muestra de opciones """

menu.columns.alignment = BeautifulTable.ALIGN_LEFT


def buscarTique() ->Tique:
    os.system('cls')
    tiquet = Tique_dao()
    print('____BUSCAR ID_____')
    print()
    ID_Tique=input('Indique un ID de TIQUE a buscar: ')
    p = tiquet.buscarTique(ID_Tique)
    if p!=None:
        print()
        print('Los datos del ID son : ',p.ID_tique,' nombre: ',p.Nombre,' Estado: ',p.Estado)
        print()
    else:
        print('ID no encontrado')
        print()
    time.sleep(5)


def eliminarTique():
    os.system('cls')
    tiquet = Tique_dao()
    print('____ELIMINAR DATOS DE TIQUE_____')
    print()
    ID_tique=input('Indique ID_tique a eliminar: ')
    print()
    print(tiquet.eliminarTique(ID_tique))
    print()
    time.sleep(3)    

def actualizarTique():
    os.system('cls')
    tiquet = Tique_dao()
    print('____Insertar Tique____')    
    print()
    ID_tique = input('indique el ID a actualizar:')
    v = tiquet.buscarTique(ID_tique)
    if v!=None:
        tiquet.actualizarTique(v)
        return
    time.sleep(5)        
        

def insertarTique():
    os.system('cls')
    tiquet = Tique_dao()
    print('____Insertar Tique____')    
    print()
    ID_tique = input('indique el ID de la persona a insertar:')
    Nombre = input('indique el nombre:').upper()
    Estado = input('indique el estado RESUELTO/ A RESOLVER:').upper()
    print(tiquet.insertarTique(Tique(ID_tique,Nombre,Estado)))
    time.sleep(5) 









def menuFuncion():  
    while True:
        print(menu)
        opcion = input('Opcion: ')
        if opcion == '1':
            buscarTique()
        elif opcion == '2':
            eliminarTique() 
        elif opcion == '3':
            insertarTique() 
        elif opcion == '4':
            actualizarTique()
        elif opcion == '5':
            loginFuncion()
            break
        elif opcion =='6':
            break 


loginFuncion()

#menu para llamar la opcion solicitada


