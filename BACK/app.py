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

@app.route("/ticket")
def obtener_estado_ticket():
    
    
    resultados = q.ejecutarSQL(q.TICKET_GET_STATUS)
    
    if not resultados:
        return jsonify({"mensaje": "No se encontraron tickets"}), 404
    

    tickets_estado = [{"id": ticket[0], "id_trackeo": ticket[1], "estado": ticket[2]} for ticket in resultados]

    return jsonify(tickets_estado)

@app.route("/ticket", methods=["POST"])
def add_ticket():
    data = (request.get_json())  # data es un diccionario de strings json, con las claves 'detallesEnvio', 'metodoPago', 'carrito' y 'total'
    total = data["total"]
    data.pop("total")  # como guardamos total en otra variable, lo eliminamos del diccionario
    data = json.dumps(data)  # convertimos el diccionario a un string json para poder guardarlo en la base de datos

    keys = ("detallesEnvio","metodoPago","carrito")  # a cada key esta asociado un valor string json que puede ser convertido a diccionario/lista
    for key in keys:
        if key not in data:
            return jsonify({"error": f"Falta el dato {key}"}), 400
        
    ticket_id = str(uuid.uuid4())
    try:
        result = q.ejecutarSQL(q.TICKET_BY_ID, {"ID_TRACKEO": ticket_id}).fetchall()

        if len(result) > 0:
            return jsonify({"error": "El ticket ya existe"}), 400
        params = {"ID_TRACKEO": ticket_id,"Total": float(total),"Payload": data,"Estado": "Autorizado"}
        q.ejecutarSQL(q.ADD_TICKET, params)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(ticket_id), 201

@app.route("/ticket/<id_trackeo>")
def obtener_estado(id_trackeo):

    result = q.ejecutarSQL(q.TICKET_BY_TRACKEO, {'id_trackeo': id_trackeo})
    
    if result:
        
        estado = result.fetchone()  
        if estado:
            return jsonify({'id_trackeo': id_trackeo, 'estado': estado[0]})
        
        return jsonify({'error': 'Ticket no encontrado'}), 404
    
    return jsonify({'error': 'Error al realizar la consulta'}), 500   


    
@app.route("/actualizarEstado", methods=["PUT"])
def actualizar_estado():
    
    data = request.get_json()

    id_trackeo = data.get("ID_TRACKEO")  
    nuevo_estado = data.get("Estado")
    
    if not id_trackeo or not nuevo_estado:
        return jsonify({"mensaje": "ID_TRACKEO y Estado son requeridos"}), 400

    try:

        q.ejecutarSQL(q.TICKET_UPDATE_STATUS, (nuevo_estado, id_trackeo))
        return jsonify({"mensaje": "Estado actualizado con éxito"}), 200
    except Exception as e:
        return jsonify({"mensaje": f"Error al actualizar estado: {str(e)}"}), 500

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

@app.route("/qr")
def obtener_qrs():
    resultados = q.ejecutarSQL(q.QR_GET_ALL)
    
    if not resultados:
        return jsonify({"mensaje": "No se encontraron qrs"}),404
    
    qrs_estado = [{"id":qr[0],"hash":qr[1],"estado": qr[2]} for qr in resultados]

    return jsonify(qrs_estado)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001,debug=True)
