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
