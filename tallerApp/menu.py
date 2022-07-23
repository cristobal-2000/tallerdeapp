from re import A
from beautifultable import BeautifulTable
from conexion import Conexion
from tique import Tique
from tique_dao import Tique_dao
from estado_tiques import Estado_Tique
from ejecutivo_dao import Ejecutivo_dao
from ejecutivo import Ejecutivo
import time
import os
"""importacion de archivos + un beautifultable para que de forma al menu + un import time para darle tiempo de respuesta"""
"""me desvele estos dias para que funcionara"""
"""me la quise jugar con una opcion de volver profe pero n ome dio el tiempo """

os.system("cls") 
Conexion.getStartConnection()

menu = BeautifulTable()
menu.columns.header=["BIENVENIDO A CENTRO DE TIQUES"]
menu.rows.append(["1.= Buscar Tique"])
menu.rows.append(["2.= Eliminar Tique"])
menu.rows.append(["3.= Insertar Tique"])
menu.rows.append(["4.= Actualizar Tique"])
"""menu para la muestra de opciones """

menu.columns.alignment = BeautifulTable.ALIGN_LEFT

def buscarTique() ->Tique:
    os.system('cls')
    tiquet = Tique_dao()
    print('____BUSCAR ID_____')
    print()
    ID_Tique=input('Indique un ID de TIQUE a buscar: ').upper()
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
    ID_tique=input('Indique ID_tique a eliminar: ').upper()
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
    ID_tique = input('indique el ID de la persona a modificar:')
    Nombre = input('indique el nombre:').upper()
    Estado = input('indique el estado RESUELTO/ A RESOLVER:').upper()
    print(tiquet.insertarTique(Tique(ID_tique,Nombre,Estado)))
    time.sleep(5) 




    
while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        buscarTique()
        break
    elif opcion == '2':
        eliminarTique()
        break  
    elif opcion == '3':
        insertarTique()
        break  
    elif opcion == '4':
        actualizarTique()
        break 

"""menu para llamar la opcion solicitada"""


