from flask import Flask, render_template, url_for, redirect, request
from user_agents import parse
import json

app = Flask(__name__)

# @app.route('/')
# def home():
#     user_agent = parse(request.headers.get('User-Agent'))
#     is_mobile = user_agent.is_mobile
#     return render_template("base.html", is_mobile=is_mobile)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/buscarProducto')
def buscar_producto():
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile 
    menus = {
        "bebidas": [
            "Agua de Jamaica", "Té Helado", "Jugo de Naranja", "Limonada", "Café Expreso"
        ],
        "carnes": [
            "Hamburguesa con Queso", "Tacos al Pastor", "Paella de Mariscos", "Fajitas de Pollo"
        ],
        "postres": [
            "Cheesecake de Fresa", "Helado de Vainilla", "Brownie de Chocolate", "Flan de Caramelo", "Tiramisú"
        ],
        "pastas frescas": [
            "Pizza Margherita", "Espaguetis a la Boloñesa", "Lasagna de Carne"
        ],
        "ensaladas y sopas": [
            "Ensalada César", "Sopa de Tomate"
        ],
        "sushi": [
            "Sushi de Salmón"
        ]

    }
    categorias = [categoria for categoria in menus ]
    return render_template("buscarproducto.html", is_mobile=is_mobile, categorias=categorias, menus=menus)

@app.route("/seguimiento")
def seguimiento():
    return render_template("seguimiento.html")


@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")


@app.route("/carrito")
def carrito():
    return render_template("carrito.html")


@app.route("/detallesEnvio", methods=["GET", "POST"])
def detallesEnvio():
    return render_template("detallesEnvio.html")


@app.route("/metodoPago", methods=["GET", "POST"])
def metodoPago():
    if request.method == "POST":
        detallesEnvio = request.form.to_dict()
        return render_template("metodoPago.html", detallesEnvio=detallesEnvio)
    return render_template("metodoPago.html")


@app.route("/confirmarCompra", methods=["GET", "POST"])
def confirmarCompra():
    if request.method == "POST":
        metodoPago = request.form.to_dict()
        detallesEnvio_json = request.form.get("detallesEnvio")
        detallesEnvio = json.loads(detallesEnvio_json)
        return render_template(
            "confirmarCompra.html", detallesEnvio=detallesEnvio, metodoPago=metodoPago
        )
    return render_template("confirmarCompra.html")


@app.route("/compraRealizada", methods=["GET", "POST"])
def compraRealizada():
    return render_template("compraRealizada.html")

""" @app.route('/compraRealizada/<id>')
def compraRealizada(id):
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile  
    return render_template("compraRealizada.html", is_mobile=is_mobile, id=id) """

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True)
