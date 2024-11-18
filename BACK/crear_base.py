import mysql.connector
from mysql.connector import Error

def crear_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678"
        )

        if conexion.is_connected():
            print("Conectado a MySQL")
            cursor = conexion.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto")
            print("Base de datos 'proyecto' lista")
        
    except Error as e:
        print("Error:", e)
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

def cargar_tablas():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="proyecto"
        )

        if conexion.is_connected():
            print("Conectado a proyecto")
            with open("base_datos.sql", "r") as archivo_sql:
                script = archivo_sql.read().split(';')

            cursor = conexion.cursor()
            for comando in script:
                if comando.strip():
                    cursor.execute(comando)
            
            print("Tablas creadas")

    except Error as e:
        print("Error :", e)
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

crear_base_datos()
cargar_tablas()
