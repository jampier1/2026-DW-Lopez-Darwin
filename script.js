/* ============================================================
   FORMULARIO DE CONTACTO (validaciones Semana 6, sin cambios)
   ============================================================ */

const formularioContacto = document.getElementById("formContacto");
const nombreContacto = document.getElementById("nombreContacto");
const emailContacto = document.getElementById("emailContacto");
const asuntoContacto = document.getElementById("asuntoContacto");
const mensajeContacto = document.getElementById("mensajeContacto");
const mensajeContactoEstado = document.getElementById("mensajeContactoEstado");

const REGEX_EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/**
 * Marca un campo como válido o inválido usando las clases de Bootstrap
 * y muestra el mensaje de error correspondiente. Función reutilizable
 * usada por ambos formularios del sitio.
 */
function actualizarEstadoCampo(campo, esValido, idError, textoError) {

    const contenedorError = document.getElementById(idError);

    if (esValido) {
        campo.classList.remove("is-invalid");
        campo.classList.add("is-valid");
        if (contenedorError) contenedorError.textContent = "";
    } else {
        campo.classList.remove("is-valid");
        campo.classList.add("is-invalid");
        if (contenedorError) contenedorError.textContent = textoError;
    }

    return esValido;
}

function validarNombreContacto() {

    const valor = nombreContacto.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(nombreContacto, false, "errorNombreContacto", "El nombre es obligatorio.");
    }

    if (valor.length < 3) {
        return actualizarEstadoCampo(nombreContacto, false, "errorNombreContacto", "El nombre debe tener al menos 3 caracteres.");
    }

    return actualizarEstadoCampo(nombreContacto, true, "errorNombreContacto", "");
}

function validarEmailContacto() {

    const valor = emailContacto.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(emailContacto, false, "errorEmailContacto", "El correo electrónico es obligatorio.");
    }

    if (!REGEX_EMAIL.test(valor)) {
        return actualizarEstadoCampo(emailContacto, false, "errorEmailContacto", "Ingrese un correo electrónico válido (ejemplo: nombre@correo.com).");
    }

    return actualizarEstadoCampo(emailContacto, true, "errorEmailContacto", "");
}

function validarAsuntoContacto() {

    const valor = asuntoContacto.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(asuntoContacto, false, "errorAsuntoContacto", "El asunto es obligatorio.");
    }

    if (valor.length < 3) {
        return actualizarEstadoCampo(asuntoContacto, false, "errorAsuntoContacto", "El asunto debe tener al menos 3 caracteres.");
    }

    return actualizarEstadoCampo(asuntoContacto, true, "errorAsuntoContacto", "");
}

function validarMensajeContacto() {

    const valor = mensajeContacto.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(mensajeContacto, false, "errorMensajeContacto", "El mensaje es obligatorio.");
    }

    if (valor.length < 10) {
        return actualizarEstadoCampo(mensajeContacto, false, "errorMensajeContacto", "El mensaje debe tener al menos 10 caracteres.");
    }

    return actualizarEstadoCampo(mensajeContacto, true, "errorMensajeContacto", "");
}

function mostrarMensajeContacto(texto, tipo) {

    mensajeContactoEstado.textContent = texto;
    mensajeContactoEstado.className = "mt-3 alert " + (tipo === "exito" ? "alert-success" : "alert-danger");

    setTimeout(function () {
        mensajeContactoEstado.textContent = "";
        mensajeContactoEstado.className = "mt-3";
    }, 4000);
}

nombreContacto.addEventListener("input", validarNombreContacto);
nombreContacto.addEventListener("blur", validarNombreContacto);

emailContacto.addEventListener("input", validarEmailContacto);
emailContacto.addEventListener("blur", validarEmailContacto);

asuntoContacto.addEventListener("input", validarAsuntoContacto);
asuntoContacto.addEventListener("blur", validarAsuntoContacto);

mensajeContacto.addEventListener("input", validarMensajeContacto);
mensajeContacto.addEventListener("blur", validarMensajeContacto);

formularioContacto.addEventListener("submit", function (event) {

    event.preventDefault();

    const nombreValido = validarNombreContacto();
    const emailValido = validarEmailContacto();
    const asuntoValido = validarAsuntoContacto();
    const mensajeValido = validarMensajeContacto();

    if (!nombreValido || !emailValido || !asuntoValido || !mensajeValido) {
        mostrarMensajeContacto("Revise los campos marcados en rojo antes de enviar.", "error");
        return;
    }

    mostrarMensajeContacto("Mensaje enviado correctamente. Nos pondremos en contacto pronto.", "exito");

    formularioContacto.reset();

    [nombreContacto, emailContacto, asuntoContacto, mensajeContacto].forEach(function (campo) {
        campo.classList.remove("is-valid", "is-invalid");
    });

});


/* ============================================================
   SECCIÓN SERVICIOS: contenido dinámico desde un arreglo de objetos
   ============================================================ */

// Los datos del catálogo viven en este arreglo, no en el HTML.
const servicios = [
    { id: 1, nombre: "Química sanguínea", descripcion: "Analiza componentes de la sangre para evaluar el funcionamiento de órganos como hígado y riñones." },
    { id: 2, nombre: "Hematología", descripcion: "Estudia las células sanguíneas para detectar anemias, infecciones y otros trastornos." },
    { id: 3, nombre: "Uroanálisis", descripcion: "Examina la orina para identificar infecciones y problemas renales." },
    { id: 4, nombre: "Pruebas rápidas", descripcion: "Resultados inmediatos para la detección temprana de enfermedades comunes." },
    { id: 5, nombre: "Coagulación", descripcion: "Evalúa la capacidad de la sangre para coagular correctamente." },
    { id: 6, nombre: "Exámenes ocupacionales", descripcion: "Certificaciones médicas requeridas para actividades laborales." },
    { id: 7, nombre: "Pruebas de embarazo", descripcion: "Detección temprana y confiable del embarazo." }
];

const listaServicios = document.getElementById("listaServicios");
const spinnerServicios = document.getElementById("spinnerServicios");
const modalServicioCuerpo = document.getElementById("modalServicioCuerpo");
const modalServicio = new bootstrap.Modal(document.getElementById("modalServicio"));

// Recorre el arreglo "servicios" (estructura repetitiva) y arma las
// tarjetas dinámicamente, evitando repetir HTML a mano. Cada tarjeta
// incluye un botón "Ver más" que abre el modal con el detalle completo.
function renderServicios() {

    listaServicios.innerHTML = "";

    servicios.forEach(function (servicio) {

        const columna = document.createElement("div");
        columna.className = "col-md-3 mb-3";

        const tarjeta = document.createElement("div");
        tarjeta.className = "card h-100";

        const cuerpo = document.createElement("div");
        cuerpo.className = "card-body d-flex flex-column";

        const titulo = document.createElement("h6");
        titulo.className = "card-title";
        titulo.textContent = servicio.nombre;

        const texto = document.createElement("p");
        texto.className = "card-text small text-muted";
        texto.textContent = servicio.descripcion;

        const botonVerMas = document.createElement("button");
        botonVerMas.type = "button";
        botonVerMas.className = "btn btn-primary btn-sm mt-auto";
        botonVerMas.textContent = "Ver más";

        botonVerMas.addEventListener("click", function () {
            modalServicioCuerpo.innerHTML = "";

            const detalleTitulo = document.createElement("h5");
            detalleTitulo.textContent = servicio.nombre;

            const detalleTexto = document.createElement("p");
            detalleTexto.textContent = servicio.descripcion;

            modalServicioCuerpo.appendChild(detalleTitulo);
            modalServicioCuerpo.appendChild(detalleTexto);

            modalServicio.show();
        });

        cuerpo.appendChild(titulo);
        cuerpo.appendChild(texto);
        cuerpo.appendChild(botonVerMas);
        tarjeta.appendChild(cuerpo);
        columna.appendChild(tarjeta);
        listaServicios.appendChild(columna);
    });
}

// Simula un pequeño proceso de carga (por ejemplo, una consulta a un
// servidor) mostrando el spinner de Bootstrap antes de renderizar.
function cargarServicios() {
    spinnerServicios.classList.remove("d-none");
    listaServicios.classList.add("d-none");

    setTimeout(function () {
        renderServicios();
        spinnerServicios.classList.add("d-none");
        listaServicios.classList.remove("d-none");
    }, 800);
}


/* ============================================================
   SECCIÓN REGISTRO DE SERVICIOS
   Validaciones dinámicas de la Semana 6 + renderizado desde un
   arreglo de objetos (Semana 7)
   ============================================================ */

const formulario = document.getElementById("formRegistro");
const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const mensaje = document.getElementById("mensaje");
const listaRegistros = document.getElementById("listaRegistros");
const total = document.getElementById("total");

const nombreRegistroEliminar = document.getElementById("nombreRegistroEliminar");
const btnConfirmarEliminar = document.getElementById("btnConfirmarEliminar");
const modalConfirmarEliminar = new bootstrap.Modal(document.getElementById("modalConfirmarEliminar"));

// Guarda temporalmente el id del registro que se quiere eliminar mientras
// se espera la confirmación del usuario en el modal.
let idRegistroPendienteEliminar = null;

const LONGITUD_MIN_NOMBRE = 3;
const LONGITUD_MIN_DESCRIPCION = 10;

// Los registros que el usuario agrega se guardan aquí, como objetos
// dentro de un arreglo, en lugar de crearse sueltos en el DOM.
let registros = [];
let siguienteId = 1;

// Validación del campo nombre
function validarNombre() {

    const valor = nombre.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(nombre, false, "errorNombre", "El nombre del servicio es obligatorio.");
    }

    if (valor.length < LONGITUD_MIN_NOMBRE) {
        return actualizarEstadoCampo(nombre, false, "errorNombre", `El nombre debe tener al menos ${LONGITUD_MIN_NOMBRE} caracteres.`);
    }

    return actualizarEstadoCampo(nombre, true, "errorNombre", "");
}

// Validación del campo descripción
function validarDescripcion() {

    const valor = descripcion.value.trim();

    if (valor === "") {
        return actualizarEstadoCampo(descripcion, false, "errorDescripcion", "La descripción es obligatoria.");
    }

    if (valor.length < LONGITUD_MIN_DESCRIPCION) {
        return actualizarEstadoCampo(descripcion, false, "errorDescripcion", `La descripción debe tener al menos ${LONGITUD_MIN_DESCRIPCION} caracteres.`);
    }

    return actualizarEstadoCampo(descripcion, true, "errorDescripcion", "");
}

// Validación del campo categoría
function validarCategoria() {

    const valor = categoria.value;

    if (valor === "") {
        return actualizarEstadoCampo(categoria, false, "errorCategoria", "Debe seleccionar una categoría.");
    }

    return actualizarEstadoCampo(categoria, true, "errorCategoria", "");
}

// Muestra un mensaje general de éxito o error debajo del formulario
function mostrarMensaje(texto, tipo) {

    mensaje.textContent = texto;
    mensaje.className = "mt-3 alert " + (tipo === "exito" ? "alert-success" : "alert-danger");

    setTimeout(function () {
        mensaje.textContent = "";
        mensaje.className = "mt-3";
    }, 4000);
}

// Crea el elemento de tarjeta (en su columna) para un registro individual
function crearTarjetaRegistro(registro) {

    const columna = document.createElement("div");
    columna.className = "col-md-6 mb-3";

    const tarjeta = document.createElement("div");
    tarjeta.className = "card p-3";

    const titulo = document.createElement("h5");
    titulo.textContent = registro.nombre;

    const texto = document.createElement("p");
    texto.textContent = registro.descripcion;

    const tipo = document.createElement("p");
    tipo.textContent = "Categoría: " + registro.categoria;

    const botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";
    botonEliminar.className = "btn btn-danger";

    // En lugar de borrar directamente, se abre el modal de confirmación.
    botonEliminar.addEventListener("click", function () {
        idRegistroPendienteEliminar = registro.id;
        nombreRegistroEliminar.textContent = registro.nombre;
        modalConfirmarEliminar.show();
    });

    tarjeta.appendChild(titulo);
    tarjeta.appendChild(texto);
    tarjeta.appendChild(tipo);
    tarjeta.appendChild(botonEliminar);
    columna.appendChild(tarjeta);

    return columna;
}

// Se ejecuta solo cuando el usuario confirma en el modal.
btnConfirmarEliminar.addEventListener("click", function () {

    if (idRegistroPendienteEliminar === null) return;

    registros = registros.filter(function (r) {
        return r.id !== idRegistroPendienteEliminar;
    });

    idRegistroPendienteEliminar = null;
    renderRegistros();
    modalConfirmarEliminar.hide();
    mostrarMensaje("Registro eliminado correctamente.", "exito");
});

// Recorre el arreglo "registros" y dibuja todas las tarjetas.
// Muestra un mensaje distinto según el estado de los datos (vacío o con registros).
function renderRegistros() {

    listaRegistros.innerHTML = "";

    if (registros.length === 0) {
        const columnaVacia = document.createElement("div");
        columnaVacia.className = "col-12";

        const vacio = document.createElement("p");
        vacio.className = "text-muted";
        vacio.textContent = "Aún no hay servicios registrados.";

        columnaVacia.appendChild(vacio);
        listaRegistros.appendChild(columnaVacia);
    } else {
        registros.forEach(function (registro) {
            listaRegistros.appendChild(crearTarjetaRegistro(registro));
        });
    }

    total.textContent = registros.length;
}

// Limpia las clases de validación al reiniciar el formulario
function limpiarValidaciones() {
    [nombre, descripcion, categoria].forEach(function (campo) {
        campo.classList.remove("is-valid", "is-invalid");
    });
}

const btnAgregarRegistro = document.getElementById("btnAgregarRegistro");
const spinnerRegistro = document.getElementById("spinnerRegistro");
const textoBtnRegistro = document.getElementById("textoBtnRegistro");

// Validación en tiempo real mientras el usuario escribe
nombre.addEventListener("input", validarNombre);
descripcion.addEventListener("input", validarDescripcion);
categoria.addEventListener("input", validarCategoria);

// Validación al perder el foco del campo
nombre.addEventListener("blur", validarNombre);
descripcion.addEventListener("blur", validarDescripcion);
categoria.addEventListener("blur", validarCategoria);

// Evento submit del formulario
formulario.addEventListener("submit", function (event) {

    // Evita que la página se recargue
    event.preventDefault();

    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    // Solo registra si todas las validaciones son correctas
    if (!nombreValido || !descripcionValida || !categoriaValida) {
        mostrarMensaje("Revise los campos marcados en rojo antes de continuar.", "error");
        return;
    }

    // Simula un breve proceso de guardado mostrando el spinner en el botón.
    btnAgregarRegistro.disabled = true;
    spinnerRegistro.classList.remove("d-none");
    textoBtnRegistro.textContent = "Guardando...";

    setTimeout(function () {

        registros.push({
            id: siguienteId++,
            nombre: nombre.value.trim(),
            descripcion: descripcion.value.trim(),
            categoria: categoria.value
        });

        renderRegistros();
        mostrarMensaje("Registro agregado correctamente.", "exito");

        formulario.reset();
        limpiarValidaciones();

        btnAgregarRegistro.disabled = false;
        spinnerRegistro.classList.add("d-none");
        textoBtnRegistro.textContent = "Agregar Servicio";

    }, 700);

});


/* ============================================================
   RENDERIZADO INICIAL AL CARGAR LA PÁGINA
   ============================================================ */

cargarServicios();
renderRegistros();