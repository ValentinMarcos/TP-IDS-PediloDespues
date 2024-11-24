import uuid
from flask import Flask, render_template, url_for, redirect, request, jsonify
from datetime import datetime
from serializer import serializador_productos
from querySql import Query_sql


q = Query_sql()
app = Flask(__name__)

@app.route("/productos")
def ver_productos():
    productos = q.ejecutarSQL(q.PRODUCTOS_GET_ALL)
    
    if not productos:
        return jsonify({})
    
    productos_por_categoria = serializador_productos(productos)
    
    return jsonify(productos_por_categoria)

@app.route("/estado")
def obtener_estado_ticket():
    
    
    resultados = q.ejecutarSQL(q.TICKET_GET_STATUS)
    
    if not resultados:
        return jsonify({"mensaje": "No se encontraron tickets"}), 404
    
  
    tickets_estado = [{"id": ticket[0], "id_trackeo": ticket[1], "estado": ticket[2]} for ticket in resultados]

    return jsonify(tickets_estado)
    
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



if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001,debug=True)
