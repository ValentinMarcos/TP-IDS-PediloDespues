// Obtener el carrito desde el Local Storage
const carrito = JSON.parse(localStorage.getItem("carrito")) || [];

// Convertir el carrito a JSON
const carritoInput = document.querySelector("#carritoInput");
if (carritoInput) {
    const carritoJSON = JSON.stringify(carrito);
    carritoInput.value = carritoJSON;
}

const resumen = crearResumenDeCompra(carrito);

document.querySelector("#contenedor-resumen").appendChild(resumen);

function crearResumenDeCompra(carrito) {
    const resumenDiv = document.createElement("div");
    resumenDiv.classList.add("resumenDiv")
    
    const titulo = document.createElement("h2");
    titulo.textContent = "Resumen de la Compra";
    resumenDiv.appendChild(titulo);
    
    const resumenUl = document.createElement("ul");
    resumenUl.classList.add("products-summary");

    let total = 0;

    // Creando un li por cada producto en el carrito
    carrito.forEach(producto => {
        const precioTotalProducto = producto.precio * producto.cantidad;

        const productLi = document.createElement("li");
        productLi.classList.add("productLi");

        const infoDiv = document.createElement("div");
        infoDiv.classList.add("infoProduct");
        productLi.appendChild(infoDiv);

        const imageDiv = document.createElement("div");
        imageDiv.classList.add("imageProduct");
        productLi.appendChild(imageDiv);

        const nombre = document.createElement("p");
        nombre.textContent = `${producto.nombre} $${producto.precio}`;
        infoDiv.appendChild(nombre);

        const cantidad = document.createElement("p");
        cantidad.textContent = `Cantidad: ${producto.cantidad}`;
        infoDiv.appendChild(cantidad);

        const precio = document.createElement("p");
        precio.textContent = `$${precioTotalProducto.toFixed(2)}`;
        infoDiv.appendChild(precio);

        const imagen = document.createElement("img");
        imagen.src = producto.img;
        imagen.alt = producto.nombre;
        imageDiv.appendChild(imagen);

        resumenUl.appendChild(productLi);

        total += precioTotalProducto;
    });

    resumenDiv.appendChild(resumenUl);


    const totalDiv = document.createElement("div");
    totalDiv.classList.add("totalDiv");

    const totalP = document.createElement("p");
    totalP.textContent = "Total:";
    totalDiv.appendChild(totalP);

    const totalCantidad = document.createElement("p");
    totalCantidad.textContent = `$${total.toFixed(2)}`;
    totalDiv.appendChild(totalCantidad);

    localStorage.setItem('total', total.toFixed(2));
    resumenDiv.appendChild(totalDiv);
    
    return resumenDiv;
}