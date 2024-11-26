// localStorage.setItem('carrito', JSON.stringify([
//     { id: 1, nombre: 'Costillas de cerdo a la Riojana', imagen: 'polloalchampignon.jpg', precio: 15, cantidad: 2},
//     { id: 4, nombre: 'Milanesa con papas fritas', imagen: 'milanesadepollo.jpg', precio: 20, cantidad: 1 },
// ]));

function cargarCarrito() {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    const carritoContenedor = document.getElementById('container-promos'); 
    carritoContenedor.textContent = '';

    if (carrito.length === 0) {
        const aviso = document.createElement('p');
        aviso.textContent = '¡No hay productos en tu carrito!';
        carritoContenedor.appendChild(aviso);

        document.getElementById('total-precio').textContent = '0.00';
        return;
    }

    let total = 0;

    const ulElemento = document.createElement('ul');
    ulElemento.classList.add('ul-box');
    carritoContenedor.appendChild(ulElemento);

    carrito.forEach((producto, index) => {
        const productoElemento = document.createElement('li');
        productoElemento.classList.add('fila');

        const cantidad = document.createElement('span');
        cantidad.classList.add('prod-cantidad');
        cantidad.textContent = producto.cantidad;

        const image = document.createElement('img');
        image.src = producto.img;
        image.classList.add('prod-imagen');
        image.alt = 'producto';

        const nombreProduct = document.createElement('p');
        nombreProduct.classList.add('prod-nombre');
        nombreProduct.textContent = producto.nombre;

        const btnMenos = document.createElement('button');
        btnMenos.classList.add('btn', 'btn-dec-cantidad');
        btnMenos.textContent = '-';
        btnMenos.onclick = () => cambiarCantidad(index, -1);

        const btnMas = document.createElement('button');
        btnMas.classList.add('btn', 'btn-inc-cantidad');
        btnMas.textContent = '+';
        btnMas.onclick = () => cambiarCantidad(index, 1);

        const precio = document.createElement('p');
        precio.classList.add('prod-precio');
        precio.textContent = "$" + producto.precio;

        const btnEliminar = document.createElement('button');
        btnEliminar.classList.add('btn', 'btn-eliminar-prod');
        btnEliminar.textContent = 'X';
        btnEliminar.onclick = () => eliminarProducto(index);

        productoElemento.appendChild(cantidad);
        productoElemento.appendChild(image);
        productoElemento.appendChild(nombreProduct);
        productoElemento.appendChild(btnMenos);
        productoElemento.appendChild(btnMas);
        productoElemento.appendChild(precio);
        productoElemento.appendChild(btnEliminar);

        ulElemento.appendChild(productoElemento);

        total += producto.precio * producto.cantidad;
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

const BTON_VACIAR_CARRITO = document.querySelector('.carrito-btn-vaciar');

BTON_VACIAR_CARRITO.addEventListener("click", () => {
    localStorage.setItem('carrito', JSON.stringify([]));
    cargarCarrito();
});

cargarCarrito();
