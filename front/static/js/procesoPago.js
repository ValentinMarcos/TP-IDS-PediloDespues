// Obtener el carrito desde el Local Storage
const carrito = JSON.parse(localStorage.getItem("carrito")) || [];

const resumen = crearResumenDeCompra(carrito);

document.querySelector("#contenedor-resumen").appendChild(resumen);

function crearResumenDeCompra(carrito) {
    const resumenDiv = document.createElement("div");
    resumenDiv.classList.add("resumenDiv")
    
    const titulo = document.createElement("h2");
    titulo.textContent = "Resumen de la Compra";
    resumenDiv.appendChild(titulo);
    
    const resumenUl = document.createElement("ul");
    resumenDiv.classList.add("products-summary");

    let total = 0;

    carrito.forEach(producto => {
        const precioTotalProducto = producto.precio * producto.cantidad;

        const productLi = document.createElement("li");
        productLi.classList.add("productLi");

        const infoDiv = document.createElement("div");
        infoDiv.classList.add("infoProduct");
        productLi.appendChild(infoDiv);

        const nombre = document.createElement("p");
        nombre.textContent = producto.nombre;
        infoDiv.appendChild(nombre);

        const cantidad = document.createElement("p");
        cantidad.textContent = `Cantidad: ${producto.cantidad}`;
        infoDiv.appendChild(cantidad);

        const precio = document.createElement("p");
        precio.textContent = `$${precioTotalProducto.toFixed(2)}`;
        infoDiv.appendChild(precio);

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

    resumenDiv.appendChild(totalDiv);

    return resumenDiv;
}