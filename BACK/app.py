from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

QUERY_VER_PRODUCTOS = "SELECT * FROM Productos"

QUERY_PRODUCTO_BY_ID = "SELECT Descripcion, Precio, Categoria FROM Productos WHERE Descripcion = :Descripcion"

QUERY_AGREGAR_PRODUCTO = "INSERT INTO Productos (Descripcion, Precio, Categoria) VALUES (:Descripcion, :Precio, :Categoria)"

def run_query(query, parameters =None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
    return result

def ver_productos():
    return run_query(QUERY_VER_PRODUCTOS).fetchall()

def agregar_producto(data):
    return run_query(QUERY_AGREGAR_PRODUCTO, data)

def producto_by_id(Descripcion):
    return run_query(QUERY_PRODUCTO_BY_ID, {'Descripcion': Descripcion}).fetchall()