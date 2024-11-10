from flask import Flask, request, redirect, render_template, url_for
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/buscarProducto")
def buscarProducto():
    return render_template("buscarproducto.html")


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


if __name__ == "__main__":
    app.run(debug=True)
