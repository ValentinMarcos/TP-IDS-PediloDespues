// Inicializa el mapa
const map = L.map('map').setView(local, 14); 

// Capa de OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '© OpenStreetMap contributors'}).addTo(map);

// Marcadores para el local y el cliente
L.marker(local).addTo(map).bindPopup("Local PediloDespues").openPopup();
L.marker(cliente).addTo(map).bindPopup("Cliente");

// Dibuja una línea entre el local y el cliente
L.polyline([local, cliente], { color: 'blue' }).addTo(map);

// Actualizando el estado del pedido
document.addEventListener("DOMContentLoaded", () => {
    var estadoActual = document.getElementById("estado-actual").innerText;
    const statusContainers = document.querySelectorAll(".status-text-container");

    let foundEstado = false; // Variable para rastrear si se encontró el estado actual

    statusContainers.forEach(container => {
        const statusPoint = container.querySelector(".status-point");
        const circle = container.querySelector(".fa-circle-check");
        if (statusPoint && statusPoint.textContent === estadoActual) {
            foundEstado = true;
            circle.classList.add("circle-done");
        }

        if (!foundEstado) {// Marca los pasos previos como completados
            circle.classList.add("circle-done");
            container.classList.add("bar-done");
        }
    });
});