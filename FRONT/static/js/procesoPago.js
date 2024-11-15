// Obtener el carrito desde el Local Storage
const carrito = JSON.parse(localStorage.getItem("carrito")) || [];

// Convertir el carrito a JSON
const carritoInput = document.querySelector("#carritoInput");
if (carritoInput) {
    const carritoJSON = JSON.stringify(carrito);
    carritoInput.value = carritoJSON;
}