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

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5001,debug=True)