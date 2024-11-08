from flask import Flask, render_template,url_for,redirect,request
from user_agents import parse

app = Flask(__name__)

# @app.route('/')
# def home():
#     user_agent = parse(request.headers.get('User-Agent'))
#     is_mobile = user_agent.is_mobile  
#     return render_template("base.html", is_mobile=is_mobile)

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



if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True)