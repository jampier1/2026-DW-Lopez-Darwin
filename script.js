// Obtener elementos del formulario
const formulario = document.getElementById("formRegistro");
const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const mensaje = document.getElementById("mensaje");
const listaRegistros = document.getElementById("listaRegistros");
const total = document.getElementById("total");

let contador = 0;

// Evento submit
formulario.addEventListener("submit", function (event) {

    // Evita que la página se recargue
    event.preventDefault();

    // Validación
    if (
        nombre.value.trim() === "" ||
        descripcion.value.trim() === "" ||
        categoria.value.trim() === ""
    ) {
        mensaje.textContent = "Todos los campos son obligatorios.";
        mensaje.className = "text-danger";
        return;
    }

    mensaje.textContent = "Registro agregado correctamente.";
    mensaje.className = "text-success";

    // Crear tarjeta
    const tarjeta = document.createElement("div");
    tarjeta.className = "card p-3 mb-3";

    // Nombre
    const titulo = document.createElement("h5");
    titulo.textContent = nombre.value;

    // Descripción
    const texto = document.createElement("p");
    texto.textContent = descripcion.value;

    // Categoría
    const tipo = document.createElement("p");
    tipo.textContent = "Categoría: " + categoria.value;

    // Botón eliminar
    const botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";
    botonEliminar.className = "btn btn-danger";

    botonEliminar.addEventListener("click", function () {

        listaRegistros.removeChild(tarjeta);

        contador--;

        total.textContent = contador;

    });

    // Agregar elementos a la tarjeta
    tarjeta.appendChild(titulo);
    tarjeta.appendChild(texto);
    tarjeta.appendChild(tipo);
    tarjeta.appendChild(botonEliminar);

    // Mostrar tarjeta
    listaRegistros.appendChild(tarjeta);

    // Actualizar contador
    contador++;
    total.textContent = contador;

    // Limpiar formulario
    formulario.reset();

});