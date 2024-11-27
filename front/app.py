import requests
from flask import Flask, render_template, url_for, redirect, request
from user_agents import parse
import json
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError

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

    categorias = [categoria for categoria in menus ]
    return render_template("home.html", is_mobile=is_mobile, categorias=categorias, menus=menus)


def obtener_coordenadas(direccion):
    try:
        geolocalizador = Nominatim(user_agent="PediloDespues")

        coordenadas = geolocalizador.geocode(direccion, exactly_one=True)

        if coordenadas:
            return coordenadas.latitude, coordenadas.longitude
        else:
            return None
    except GeopyError as e:
        print(f"Error al obtener coordenadas: {e}")
        return None


@app.route("/seguimiento", methods=["GET", "POST"])
def seguimiento():
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    if request.method == "POST":
        try:
            codigo = request.form.get("codigo")

            response = requests.get(f"{API_URL}/tickets/{codigo}")
            response.raise_for_status()
            return redirect( url_for('estadoPedido', codigo = codigo))
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP: {e}")
        except Exception as e:
            print(f"Error fetching data: {e}")
    return render_template("seguimiento.html",is_mobile=is_mobile)

@app.route("/estadoPedido/<codigo>")
def estadoPedido(codigo):
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    response = requests.get(f"{API_URL}/tickets/{codigo}")
    response.raise_for_status()

    datos = response.json()
    payload = datos["Payload"]
    datos.pop("Payload")
    payload = json.loads(payload)
    detallesEnvio = json.loads(payload["detallesEnvio"])
    metodoPago = json.loads(payload["metodoPago"])
    carrito = json.loads(payload["carrito"])
    detallesEnvio['coordenadas'] = [-34.60377894667502, -58.410986509306255]
    try:
        coordenadas_cliente = obtener_coordenadas(detallesEnvio["direccion"])
        if coordenadas_cliente:
            detallesEnvio["coordenadas"] = coordenadas_cliente
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Error fetching data: {e}")
    return render_template("estadoPedido.html",codigo=codigo,datos=datos,detallesEnvio=detallesEnvio,
                                    metodoPago=metodoPago,carrito=carrito,is_mobile=is_mobile)

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


@app.route("/guardarCompra", methods=["POST"])
def guardarCompra():
    try:
        response = requests.post(API_URL + "/ticket", json=request.form.to_dict())
        response.raise_for_status()
        id = response.json()
    except requests.exceptions.RequestException as e:
        print(f"error data : {e}")
        id = None
    return redirect(url_for("compraRealizada", id=id))


@app.route("/compraRealizada/<id>")
def compraRealizada(id):
    user_agent = parse(request.headers.get("User-Agent"))
    is_mobile = user_agent.is_mobile
    return render_template("compraRealizada.html", is_mobile=is_mobile, id=id)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
