// localStorage.setItem('carrito', JSON.stringify([
//     { id: 1, nombre: 'Costillas de cerdo a la Riojana', imagen: 'polloalchampignon.jpg', precio: 15, cantidad: 2},
//     { id: 4, nombre: 'Milanesa con papas fritas', imagen: 'milanesadepollo.jpg', precio: 20, cantidad: 1 },
// ]));

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
    

    const ulElemento = document.createElement('ul');
    ulElemento.classList.add('ul-box');
    
    carritoContenedor.appendChild(ulElemento);

    carrito.forEach((producto, index) => {
        const productoElemento = document.createElement('li');
        productoElemento.classList.add('fila');
        productoElemento.innerHTML += `
           <span class="prod-cantidad">${producto.cantidad}</span>
           <img src="${producto.img}" class="prod-imagen" alt="producto">
           <p class="prod-nombre">${producto.nombre}</p>
           <button class="btn btn-dec-cantidad" onclick="cambiarCantidad(${index}, -1)">-</button>
           <button class="btn btn-inc-cantidad" onclick="cambiarCantidad(${index}, 1)">+</button>
           <p class="prod-precio">$${producto.precio}</p>
           <button class="btn btn-eliminar-prod" onclick="eliminarProducto(${index})">X</button>
        `;
        
        total += producto.precio * producto.cantidad;

        ulElemento.appendChild(productoElemento);
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