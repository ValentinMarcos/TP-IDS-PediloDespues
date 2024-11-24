import requests
from flask import Flask, render_template, url_for, redirect, request
from user_agents import parse
import json

API_URL = "http://localhost:5001"

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    categorias = []
    menus = {}
    try:
        data = requests.get(API_URL + "/productos")
        data.raise_for_status()
        menus = data.json()
        categorias = [categoria for categoria in menus]
    except requests.exceptions.RequestException as e:
        print(f"error data : {e}")

        "pollo": [{"nombre":''.join(items.split(',')[0]).lower(), "img":"static/images/"+ ''.join(items.lower().split(',')[0].split(" ")) + ".jpg", "precio": items.split(",")[1] } for items in ["Pollo al champignon,12000", "Pollo al horno,9000", "Milanesa de pollo,6000", "Pollo al espiedo,15000", "Pollo frito,12000"]],
        
        "acompañamientos": [{"nombre":''.join(items.split(',')[0]).lower(), "img":"static/images/"+ ''.join(items.lower().split(',')[0].split(" ")) + ".jpg", "precio": items.split(",")[1] } for items in ["Papas fritas,3000", "Pure de papas,2000", "Ensalada mixta,3500", "Aros de cebolla,2000"]],
        
        "postres": [{"nombre":''.join(items.split(',')[0]).lower(), "img":"static/images/"+ ''.join(items.lower().split(',')[0].split(" ")) + ".jpg", "precio": items.split(",")[1] } for items in ["Flan,6000", "Brownie,4000", "Cheesecake,5000", "Tiramisu,7000", "Helado,7000"]],
    }

    categorias = [categoria for categoria in menus ]
    return render_template("home.html", is_mobile=is_mobile, categorias=categorias, menus=menus)

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
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    return render_template("detallesEnvio.html", is_mobile=is_mobile)


@app.route("/metodoPago", methods=["GET", "POST"])
def metodoPago():
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    if request.method == "POST":
        detallesEnvio = request.form.to_dict()
        return render_template(
            "metodoPago.html", is_mobile=is_mobile, detallesEnvio=detallesEnvio
        )
    return render_template("metodoPago.html", is_mobile=is_mobile)


@app.route("/confirmarCompra", methods=["GET", "POST"])
def confirmarCompra():
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    if request.method == "POST":
        metodoPago = request.form.to_dict()
        detallesEnvio_json = request.form.get("detallesEnvio")
        detallesEnvio = json.loads(detallesEnvio_json)
        return render_template("confirmarCompra.html",is_mobile=is_mobile, detallesEnvio=detallesEnvio, metodoPago=metodoPago,
        )
    return render_template("confirmarCompra.html", is_mobile=is_mobile)


@app.route("/compraRealizada", methods=["GET", "POST"])
def compraRealizada():
    return render_template("compraRealizada.html")


""" @app.route('/compraRealizada/<id>')
def compraRealizada(id):
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile  
    return render_template("compraRealizada.html", is_mobile=is_mobile, id=id) """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
