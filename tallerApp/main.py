from conexion import Conexion

def login():
    print("Sistema de Tickets")
    usuario=input("ingrese usuario:")
    password=input("ingrese contraseña")
    usuario2 = "(\'%s\',)"%(usuario)
    password2 = "(\'%s\',)"%(password)
    
    #con un cursor hacemos una consulta sql para obtener los usuarios
    Conexion.cursor.execute("SELECT CORREO FROM EJECUTIVO")
    #la funcion fetchall toda lo que obtuvimos con la consulta y lo pasa a una lista python
    usuarios = Conexion.cursor.fetchall()
    Conexion.cursor.execute("SELECT CONTRASENA FROM EJECUTIVO")
    password= Conexion.cursor.fetchall()
    
    for i in usuarios:
        i=str(i)
        print(i)
        print(usuario2)
        if i == usuario2:
            print("usuario correcto")
            break
        else:
            print("usuario incorrecto")

    for x in password:
        x=str(x)
        if x == password2:
            print("contraseña correcta")
            break
        else:
            print("contraseña incorrecta")


    while True:
        try:
            for x in password:
                x=str(x)
                print(x)
                print(password2)
                if x == password2:
                    print("contraseña correcta")
                    break
        except:
            print("Contraseña incorrecta")
            password2=input("Ingrese nuevamente la contraseña")
            break


    print(usuarios)

login()


