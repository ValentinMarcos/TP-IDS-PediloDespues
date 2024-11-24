import uuid
from flask import Flask, render_template, url_for, redirect, request, jsonify
from datetime import datetime
from serializer import serializador_productos
from querySql import Query_sql
import json


q = Query_sql()
app = Flask(__name__)

@app.route("/productos")
def ver_productos():
    productos = q.ejecutarSQL(q.PRODUCTOS_GET_ALL)
    
    if not productos:
        return jsonify({})
    
    productos_por_categoria = serializador_productos(productos)
    
    return jsonify(productos_por_categoria)

@app.route("/cargardatos")
def cargar_datos():
    cvs = [
        ['Coca cola', '3000.00', 'bebidas' ], 
        ['Vino tinto', '6000.00', 'bebidas'], 
        ['Milanesa de pollo', '7000.00', 'carnes'],
        ['Pollo al horno', '7000.00', 'carnes'], 
        ['Papas fritas', '2000.00', 'acompañamientos'],
        ['Ensalada mixta', '2000.00', 'acompañamientos'], 
        ['Flan', '4000.00', 'postres'],
        ['Helado', '4000.00', 'postres']        
    ]

    for Descripcion, Precio, Categoria in cvs:
        q.ejecutarSQL(q.PRODUCTOS_ADD, {"Descripcion" : Descripcion, "Precio": Precio, "Categoria" : Categoria})

    return jsonify({"mensaje" : "se cargaron los datos correctamente"})


@app.route("/ticket", methods=["POST"])
def add_ticket():
    data = (request.get_json())  # data es un diccionario de strings json, con las claves 'detallesEnvio', 'metodoPago', 'carrito' y 'total'
    total = data["total"]
    data.pop("total")  # como guardamos total en otra variable, lo eliminamos del diccionario
    data = json.dumps(data)  # convertimos el diccionario a un string json para poder guardarlo en la base de datos
    print("El tamaño de data es:", len(data))

    keys = ("detallesEnvio","metodoPago","carrito")  # a cada key esta asociado un valor string json que puede ser convertido a diccionario/lista
    for key in keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400
        
    ticket_id = str(uuid.uuid4())
    try:
        result = q.ejecutarSQL(q.TICKET_BY_ID, {"ID": ticket_id}).fetchall()

        if len(result) > 0:
            return jsonify({"error": "El ticket ya existe"}), 400
        params = {"ID": ticket_id,"Total": float(total),"Payload": data,"Estado": "Autorizado","FechaCreacion": datetime.now()}
        q.ejecutarSQL(q.ADD_TICKET, params)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(ticket_id), 201


@app.route("/ticket/<id>", methods=["GET"])
def get_ticket(id):
    try:
        result = q.ejecutarSQL(q.TICKET_BY_ID, {"ID": id}).fetchone()

        if not result:
            return jsonify({"error": "No se encontró el ticket"}), 404

        # convierte el resultado en un diccionario
        keys = ["ID", "Total", "Payload", "Estado", "FechaCreacion"]
        ticket = dict(zip(keys, result))

        return jsonify(ticket), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001,debug=True)
