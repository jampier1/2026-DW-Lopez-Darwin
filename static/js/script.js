const formulario = document.getElementById("formContacto");

const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const tipoSolicitud = document.getElementById("tipoSolicitud");
const asunto = document.getElementById("asunto");
const mensaje = document.getElementById("mensaje");
const mensajeFormulario = document.getElementById("mensajeFormulario");
const spinnerCarga = document.getElementById("spinnerCarga");

const errorNombre = document.getElementById("errorNombre");
const errorCorreo = document.getElementById("errorCorreo");
const errorTipo = document.getElementById("errorTipo");
const errorAsunto = document.getElementById("errorAsunto");
const errorMensaje = document.getElementById("errorMensaje");

const listaSolicitudes = document.getElementById("listaSolicitudes");
const totalRegistros = document.getElementById("totalRegistros");

let contador = 0;

let solicitudes = [];

function validarNombre() {

    if (nombre.value.trim() === "") {

        errorNombre.textContent = "Ingrese su nombre";
        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        return false;
    }

    if (nombre.value.trim().length < 3) {

        errorNombre.textContent = "El nombre debe tener al menos 3 caracteres.";
        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        return false;
    }

    errorNombre.textContent = "";
    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");

    return true;

}

function validarCorreo() {

    let formatoCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    if (correo.value.trim() === "") {

        errorCorreo.textContent = "Ingrese su correo electrónico";
        correo.classList.add("is-invalid");
        correo.classList.remove("is-valid");

        return false;
    }


    if (!formatoCorreo.test(correo.value)) {

        errorCorreo.textContent = "Ingrese un correo válido";
        correo.classList.add("is-invalid");
        correo.classList.remove("is-valid");

        return false;
    }


    errorCorreo.textContent = "";
    correo.classList.remove("is-invalid");
    correo.classList.add("is-valid");

    return true;

}

function validarTipo() {

    if (tipoSolicitud.value === "") {

        errorTipo.textContent = "Seleccione un tipo de solicitud";
        tipoSolicitud.classList.add("is-invalid");
        tipoSolicitud.classList.remove("is-valid");

        return false;
    }

    errorTipo.textContent = "";
    tipoSolicitud.classList.remove("is-invalid");
    tipoSolicitud.classList.add("is-valid");

    return true;

}

function validarAsunto() {

    if (asunto.value.trim() === "") {

        errorAsunto.textContent = "Ingrese un asunto";
        asunto.classList.add("is-invalid");
        asunto.classList.remove("is-valid");

        return false;
    }

    errorAsunto.textContent = "";
    asunto.classList.remove("is-invalid");
    asunto.classList.add("is-valid");

    return true;

}

function validarMensaje() {

    if (mensaje.value.trim() === "") {

        errorMensaje.textContent = "Ingrese un mensaje";
        mensaje.classList.add("is-invalid");
        mensaje.classList.remove("is-valid");

        return false;
    }

    if (mensaje.value.trim().length < 15) {

        errorMensaje.textContent = "El mensaje debe tener al menos 15 caracteres.";
        mensaje.classList.add("is-invalid");
        mensaje.classList.remove("is-valid");

        return false;
    }

    errorMensaje.textContent = "";
    mensaje.classList.remove("is-invalid");
    mensaje.classList.add("is-valid");

    return true;

}

function mostrarSolicitudes() {

    listaSolicitudes.innerHTML = "";

    if (solicitudes.length === 0) {

    listaSolicitudes.innerHTML =
    '<div class="alert alert-info">No existen solicitudes registradas.</div>';

    return;
}

    solicitudes.forEach(function (solicitud, indice) {

        const tarjeta = document.createElement("div");

        tarjeta.className = "card shadow-sm p-3 mb-3";

        tarjeta.innerHTML = `
            <p><strong>Nombre:</strong> ${solicitud.nombre}</p>
            <p><strong>Correo:</strong> ${solicitud.correo}</p>
            <p><strong>Tipo de Solicitud:</strong> ${solicitud.tipo}</p>
            <p><strong>Asunto:</strong> ${solicitud.asunto}</p>
            <p><strong>Mensaje:</strong> ${solicitud.mensaje}</p>
            <button class="btn btn-danger btn-sm mt-3">
                Eliminar
            </button>
        `;

        tarjeta.querySelector("button").addEventListener("click", function () {

            solicitudes.splice(indice, 1);

            contador--;

            totalRegistros.textContent = contador;

            mostrarSolicitudes();

        });

        listaSolicitudes.appendChild(tarjeta);

    });

}
formulario.addEventListener("submit", function (evento) {

    evento.preventDefault();

    errorNombre.textContent = "";
    errorCorreo.textContent = "";
    errorTipo.textContent = "";
    errorAsunto.textContent = "";
    errorMensaje.textContent = "";

    nombre.classList.remove("is-invalid");
    correo.classList.remove("is-invalid");
    tipoSolicitud.classList.remove("is-invalid");
    asunto.classList.remove("is-invalid");
    mensaje.classList.remove("is-invalid");

    let valido = true;

    if (!validarNombre()) {
    valido = false;
    }

    if (!validarCorreo()) {
    valido = false;
    }

    if (!validarTipo()) {
    valido = false;
    }

    if (!validarAsunto()) {
    valido = false;
    }
    
    if (!validarMensaje()) {
    valido = false;
    }

    if (!valido) {

        mensajeFormulario.innerHTML =
        '<div class="alert alert-danger">Corrija los errores antes de enviar el formulario.</div>';
        
        return;
    }

    spinnerCarga.classList.remove("d-none");

setTimeout(function () {

    const nuevaSolicitud = {

        nombre: nombre.value,
        correo: correo.value,
        tipo: tipoSolicitud.value,
        asunto: asunto.value,
        mensaje: mensaje.value

    };

    solicitudes.push(nuevaSolicitud);

    mostrarSolicitudes();

    contador++;

    totalRegistros.textContent = contador;

    mensajeFormulario.innerHTML =
    '<div class="alert alert-success">Solicitud registrada correctamente.</div>';

    spinnerCarga.classList.add("d-none");

    formulario.reset();

    nombre.classList.remove("is-valid");
    correo.classList.remove("is-valid");
    tipoSolicitud.classList.remove("is-valid");
    asunto.classList.remove("is-valid");
    mensaje.classList.remove("is-valid");

}, 2000);

});

nombre.addEventListener("input", validarNombre);
nombre.addEventListener("blur", validarNombre);

correo.addEventListener("input", validarCorreo);
correo.addEventListener("blur", validarCorreo);

tipoSolicitud.addEventListener("change", validarTipo);

asunto.addEventListener("blur", validarAsunto);

mensaje.addEventListener("input", validarMensaje);
mensaje.addEventListener("blur", validarMensaje)

mostrarSolicitudes();