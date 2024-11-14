// Función para mostrar u ocultar el menú desplegable
function toggleDropdown() {
    var dropdown = document.getElementById("navbar-dropdown");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

// Cerrar el menú cuando se hace clic fuera de él
window.onclick = function(event) {
    if (!event.target.matches('.navbar-user-icon')) {
        var dropdown = document.getElementById("navbar-dropdown");
        if (dropdown && dropdown.style.display === "block") {
            dropdown.style.display = "none";
        }
    }
};
