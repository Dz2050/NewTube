document.addEventListener('DOMContentLoaded', function() {
    const idInput = document.getElementById("usuario_id");
    const nombreInput = document.getElementById("usuario_nombre");
    const cantidadVideosInput = document.getElementById("usuario_cantidad_videos");
    const tituloInput = document.getElementById("id_titulo");
    const aceptarButton = document.getElementById("botonAceptar");
    const siButton = document.getElementById('botonSi');
    const noButton = document.getElementById('botonNo');

    const confirmacionDiv = document.getElementById("confirmacion");
    const nombreUsuarioSpan = document.getElementById("nombre-usuario");
    const numeroIdSpan = document.getElementById("numero-id");
    const cantidadVideosConfirmacionSpan = document.getElementById("cantidad-videos-confirmacion");
    const datosUsuarioDiv = document.getElementById("datos-usuario");
    const datosVideoDiv = document.getElementById("datos-video");
    const videoForm = document.getElementById("video-form");

    function validarFormulario() {
        let datosValidos = true;

        const id = idInput.value;
        if (!/^\d{5}$/.test(id)) {
            alert("El ID debe tener 5 caracteres numéricos.");
            datosValidos = false;
        }

        const nombre = nombreInput.value;
        if (nombre.trim() === "") {
            alert("El nombre no puede estar vacío.");
            datosValidos = false;
        }

        const cantidadVideos = parseInt(cantidadVideosInput.value);
        if (isNaN(cantidadVideos) || cantidadVideos < 1) {
            alert("La cantidad de videos debe ser de al menos 1.");
            datosValidos = false;
        }

        if (datosVideoDiv.style.display === 'block') {
            const archivo = archivoInput.value;
            if (archivo.trim() === "") {
                alert("Debes seleccionar un archivo de video.");
                datosValidos = false;
            }
        }

        if (datosValidos) {
            mostrarConfirmacion();
        } else {
            alert("Por favor, corrige los errores en el formulario");
        }
    }

function mostrarConfirmacion() {
    nombreUsuarioSpan.textContent = nombreInput.value;
    numeroIdSpan.textContent = idInput.value;
    cantidadVideosConfirmacionSpan.textContent = cantidadVideosInput.value;
    confirmacionDiv.style.display = 'block';
    datosUsuarioDiv.style.display = 'none';
}

    function mostrarFormularioVideo() {
        datosVideoDiv.style.display = 'block';
        confirmacionDiv.style.display = 'none';
    }   

        function cancelarSubida() {
            confirmacionDiv.style.display = 'none';
        }

    
    aceptarButton.addEventListener('click', validarFormulario);
    siButton.addEventListener('click', mostrarFormularioVideo);
    noButton.addEventListener('click', cancelarSubida);
});
