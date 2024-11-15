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
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile
    promo_images = [
        'images/Promos/Promo docena de empanadas.png',
        'images/Promos/Promo Costillas de cerdo a la Riojana.png',
        'images/Promos/Promo Milanesa a Caballo.png',
        'images/Promos/Promo Milanesa con Papas Fritas.png'
    ]
    return render_template("home.html", is_mobile=is_mobile, promo_images=promo_images)

@app.route('/buscarProducto')
def buscarProducto():
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile 
    menus = {
        "bebidas": [{items:"static/images/"+ ''.join(items.lower().split(' ')) + ".jpg"} for items in ["Coca Cola", "Vino Tinto", "Agua Mineral", "Jugo de Naranja", "Gaseosa", "Cafe Expresso"]],

        "pollo": [{items:"static/images/"+ ''.join(items.lower().split(' ')) + ".jpg"} for items in ["Pollo al champignon", "Pollo al horno", "Milanesa de pollo", "Pollo al espiedo", "Pollo frito"]],
        
        "acompañamientos": [{items:"static/images/"+ ''.join(items.lower().split(' ')) + ".jpg"} for items in ["Papas fritas", "Pure de papas", "Ensalada mixta", "Aros de cebolla"]],
        
        "postres": [{items:"static/images/"+ ''.join(items.lower().split(' ')) + ".jpg"} for items in ["Flan", "Brownie", "Cheesecake", "Tiramisu", "Helado"]],
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
    ticket_id = request.args.get("ticket_id")
    return render_template("compraRealizada.html", ticket_id=ticket_id)

@app.route("/endpointApropiado", methods=["POST"])
def endpointApropiado():

    # Obtener los datos del formulario
    detalles_envio = request.form.get("detallesEnvio")  # JSON string
    metodo_pago = request.form.get("metodoPago")  # JSON string
    carrito_json = request.form.get("carrito")  # JSON string

    # Convertir de JSON string a Python dict/list
    detalles_envio = json.loads(detalles_envio)
    metodo_pago = json.loads(metodo_pago)
    carrito = json.loads(carrito_json)


    return render_template("compraRealizada.html")

""" @app.route('/compraRealizada/<id>')
def compraRealizada(id):
    user_agent = parse(request.headers.get('User-Agent'))
    is_mobile = user_agent.is_mobile  
    return render_template("compraRealizada.html", is_mobile=is_mobile, id=id) """

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True)
