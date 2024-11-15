from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

QUERY_VER_PRODUCTOS = "SELECT * FROM Productos"

QUERY_PRODUCTO_BY_ID = "SELECT Descripcion, Precio, Categoria FROM Productos WHERE Descripcion = :Descripcion"

QUERY_AGREGAR_PRODUCTO = "INSERT INTO Productos (Descripcion, Precio, Categoria) VALUES (:Descripcion, :Precio, :Categoria)"

engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3306/proyecto")

def run_query(query, parameters=None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), parameters)
            conn.commit()  
            return result
    except SQLAlchemyError as e:
        print(f"Error en la consulta: {e}")
        return None

def ver_productos():
    result = run_query(QUERY_VER_PRODUCTOS)
    if result:
        return result.fetchall()
    return []

def agregar_producto(data):
    result = run_query(QUERY_AGREGAR_PRODUCTO, data)
    if result:
        return result.rowcount
    return 0

def producto_by_id(Descripcion):
    result = run_query(QUERY_PRODUCTO_BY_ID, {'Descripcion': Descripcion})
    if result:
        return result.fetchall()
    return []

if __name__ == "__main__":
    print(ver_productos())