import uuid
from flask import Flask, render_template, url_for, redirect, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


QUERY_VER_PRODUCTOS = "SELECT * FROM Productos"

QUERY_PRODUCTO_BY_ID = "SELECT Descripcion, Precio, Categoria FROM Productos WHERE Descripcion = :Descripcion"

QUERY_AGREGAR_PRODUCTO = "INSERT INTO Productos (Descripcion, Precio, Categoria) VALUES (:Descripcion, :Precio, :Categoria)"

QUERY_AGREGAR_TICKET = "INSERT INTO Tickets (Total, Payload, Estado, FechaCreacion) VALUES (:Total, :Payload, :Estado, :FechaCreacion)"

QUERY_VER_TICKETS = "SELECT * FROM Tickets"

engine = create_engine("mysql+mysqlconnector://root:12345678@localhost:3306/proyecto")

app = Flask(__name__)


def run_query(query, parameters=None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), parameters)
            conn.commit()  
            return result
    except SQLAlchemyError as e:
        print(f"Error en la consulta: {e}")
        return None

@app.route("/api/VerProductos")
def ver_productos():
    productos = run_query(QUERY_VER_PRODUCTOS)
    
    if not productos:
        return jsonify({})
    
    productos_por_categoria = {}

    for producto in productos:
        descripcion,precio,categoria = producto

        if categoria not in productos_por_categoria:
            productos_por_categoria[categoria] = []
        productos_por_categoria[categoria].append({'nombre': descripcion,'precio':precio})
    
    return jsonify(productos_por_categoria)


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

def agregar_ticket(total, carrito, estado = "Pendiente"):
    payload = str(carrito)
    ticket_id = (uuid.uuid4())
    fecha_creacion = datetime.now()
    params = {
        'ID': ticket_id,
        'Total': total,
        'Payload': payload,
        'Estado': estado,
        'FechaCreacion': fecha_creacion,
    }
    result = run_query(QUERY_AGREGAR_TICKET, params)
    if result:
        return ticket_id
    return 0

def ver_tickets():
    result = run_query(QUERY_VER_TICKETS)
    if result:
        return result.fetchall()
    return []

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001,debug=True)
    print(ver_productos())