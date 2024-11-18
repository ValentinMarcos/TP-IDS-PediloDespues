import mysql.connector
from mysql.connector import Error

def check_database_and_table():
    try:
        # Conectar a MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678"
        )

        if conexion.is_connected():
            print("Conectado a MySQL")

            # Verificar si la base de datos 'proyecto' existe
            cursor = conexion.cursor()
            cursor.execute("SHOW DATABASES LIKE 'proyecto'")
            database_exists = cursor.fetchone()
            if database_exists:
                print("La base de datos 'proyecto' existe")

                
                conexion.database = 'proyecto'

                # Verificar si la tabla 'Productos' existe
                cursor.execute("SHOW TABLES LIKE 'Productos'")
                table_exists = cursor.fetchone()
                if table_exists:
                    print("La tabla 'Productos' existe")
                else:
                    print("La tabla 'Productos' no existe")
            else:
                print("La base de datos 'proyecto' no existe")

    except Error as e:
        print("Error:", e)
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    check_database_and_table()