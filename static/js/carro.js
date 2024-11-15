/*localStorage.setItem('carrito', JSON.stringify([
    { id: 1, nombre: 'Costillas de cerdo a la Riojana', precio: 15, cantidad: 2 },
    { id: 4, nombre: 'Milanesa con papas fritas', precio: 20, cantidad: 1 },
]));*/

function cargarCarrito() {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    const carritoContenedor = document.getElementById('container-promos'); 
    carritoContenedor.innerHTML = '';

    if (carrito.length === 0) {
        carritoContenedor.innerHTML = '<p>¡No hay productos en tu carrito!</p>';
        document.getElementById('total-precio').textContent = '0.00';
        return;
    }

    let total = 0;

    carrito.forEach((producto, index) => {
        const productoElemento = document.createElement('div');
        productoElemento.classList.add('col-12', 'mb-3');
        productoElemento.innerHTML = `
            <div class="card p-3">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <h5 class="producto-nombre">${producto.nombre}</h5>
                        <p class="producto-precio">Precio: $${producto.precio}</p>
                        <div>
                            <button onclick="cambiarCantidad(${index}, -1)" class="btn btn-sm btn-secondary">-</button>
                            <span class="mx-2">${producto.cantidad}</span>
                            <button onclick="cambiarCantidad(${index}, 1)" class="btn btn-sm btn-secondary">+</button>
                        </div>
                    </div>
                    <button onclick="eliminarProducto(${index})" class="btn btn-danger">Eliminar</button>
                </div>
            </div>
        `;

        total += producto.precio * producto.cantidad;

        carritoContenedor.appendChild(productoElemento);
    });

    document.getElementById('total-precio').textContent = total.toFixed(2);
}

function eliminarProducto(index) {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.splice(index, 1);
    localStorage.setItem('carrito', JSON.stringify(carrito));
    cargarCarrito();
}

function cambiarCantidad(index, cantidad) {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito[index].cantidad += cantidad;

    if (carrito[index].cantidad < 1) carrito[index].cantidad = 1;

    localStorage.setItem('carrito', JSON.stringify(carrito));
    cargarCarrito();
}

const BTON_VACIAR_CARRITO = document.querySelector('.carrito-btn-vaciar')

BTON_VACIAR_CARRITO.addEventListener("click", () =>{
    localStorage.setItem('carrito', JSON.stringify([]))
    cargarCarrito()
})

cargarCarrito();