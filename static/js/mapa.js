function obtenerUbicacionUsuario() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            console.log("Ubicación del usuario:", lat, lon);
            // Aquí puedes agregar la lógica para centrar el mapa en la ubicación
        });
    } else {
        alert("Geolocalización no es compatible con este navegador.");
    }
}

window.onload = obtenerUbicacionUsuario;
