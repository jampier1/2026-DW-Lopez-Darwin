from flask import Flask, render_template

app = Flask(__name__)


# Información general del sistema
informacion_sistema = {
    "nombre": "BanGYE Digital",
    "descripcion": "Sistema web de gestión de solicitudes y servicios financieros",
    "ciudad": "Guayaquil, Ecuador",
    "horario": "Lunes a Viernes de 8:00 AM a 17:00 PM"
}


# Servicios disponibles en el sistema
servicios = [
    {
        "nombre": "Cuentas Bancarias",
        "descripcion": "Gestión y seguimiento de movimientos financieros."
    },
    {
        "nombre": "Transferencias",
        "descripcion": "Envío y recepción de dinero de forma rápida y confiable."
    },
    {
        "nombre": "Banca Digital",
        "descripcion": "Acceso a información financiera mediante la plataforma."
    },
    {
        "nombre": "Pagos Seguros",
        "descripcion": "Gestión de pagos digitales de forma segura y cómoda."
    }
]


# Solicitudes de ejemplo
solicitudes_registradas = [
    {
        "id": "001",
        "cliente": "María González",
        "tipo": "Apertura de cuenta",
        "asunto": "Solicitud de apertura de cuenta bancaria",
        "fecha": "12/08/2026",
        "estado": "Pendiente"
    },
    {
        "id": "002",
        "cliente": "Carlos Mendoza",
        "tipo": "Consulta de saldo",
        "asunto": "Consulta de saldo disponible",
        "fecha": "13/08/2026",
        "estado": "Atendida"
    },
    {
        "id": "003",
        "cliente": "Andrea López",
        "tipo": "Transferencia",
        "asunto": "Consulta sobre transferencia nacional",
        "fecha": "14/08/2026",
        "estado": "Pendiente"
    }
]


# Información de cuentas
cuentas_bancarias = [
    {
        "numero": "001-000123",
        "titular": "María González",
        "tipo": "Cuenta de Ahorros",
        "descripcion": "Cuenta destinada al ahorro y administración de fondos.",
        "fecha": "05/06/2026",
        "estado": "Activa"
    },
    {
        "numero": "001-000456",
        "titular": "Carlos Mendoza",
        "tipo": "Cuenta Corriente",
        "descripcion": "Cuenta para gestionar operaciones y movimientos financieros.",
        "fecha": "21/06/2026",
        "estado": "Activa"
    },
    {
        "numero": "001-000789",
        "titular": "Andrea López",
        "tipo": "Cuenta Digital",
        "descripcion": "Cuenta para realizar operaciones mediante canales digitales.",
        "fecha": "10/07/2026",
        "estado": "Pendiente"
    },
    {
        "numero": "001-000812",
        "titular": "José Ramírez",
        "tipo": "Cuenta de Ahorros",
        "descripcion": "Cuenta destinada al ahorro y administración de fondos.",
        "fecha": "28/07/2026",
        "estado": "Activa"
    }
]


# Transferencias de ejemplo
transferencias_realizadas = [
    {
        "numero": "TRX-0001",
        "tipo": "Transferencia nacional",
        "origen": "001-000123",
        "destino": "001-000456",
        "fecha": "11/08/2026",
        "monto": 250.00,
        "estado": "Completada"
    },
    {
        "numero": "TRX-0002",
        "tipo": "Transferencia nacional",
        "origen": "001-000789",
        "destino": "001-000812",
        "fecha": "12/08/2026",
        "monto": 125.50,
        "estado": "Completada"
    },
    {
        "numero": "TRX-0003",
        "tipo": "Transferencia nacional",
        "origen": "001-000456",
        "destino": "001-000123",
        "fecha": "14/08/2026",
        "monto": 80.00,
        "estado": "Pendiente"
    },
    {
        "numero": "TRX-0004",
        "tipo": "Transferencia nacional",
        "origen": "001-000812",
        "destino": "001-000789",
        "fecha": "15/08/2026",
        "monto": 320.00,
        "estado": "Completada"
    }
]


# Pagos de ejemplo
pagos_disponibles = [
    {
        "numero": "PAG-0001",
        "cuenta": "001-000123",
        "concepto": "Servicio de internet",
        "fecha": "10/08/2026",
        "monto": 45.00,
        "estado": "Completado"
    },
    {
        "numero": "PAG-0002",
        "cuenta": "001-000456",
        "concepto": "Servicio eléctrico",
        "fecha": "11/08/2026",
        "monto": 62.75,
        "estado": "Completado"
    },
    {
        "numero": "PAG-0003",
        "cuenta": "001-000789",
        "concepto": "Servicio de agua potable",
        "fecha": "13/08/2026",
        "monto": 28.50,
        "estado": "Pendiente"
    },
    {
        "numero": "PAG-0004",
        "cuenta": "001-000812",
        "concepto": "Pago de tarjeta",
        "fecha": "14/08/2026",
        "monto": 150.00,
        "estado": "Completado"
    }
]


@app.route("/")
def inicio():
    return render_template(
        "index.html",
        informacion=informacion_sistema,
        servicios=servicios
    )


@app.route("/solicitudes")
def solicitudes():
    return render_template(
        "solicitudes.html",
        solicitudes=solicitudes_registradas,
        informacion=informacion_sistema
    )


@app.route("/cuentas")
def cuentas():
    return render_template(
        "cuentas.html",
        cuentas=cuentas_bancarias,
        informacion=informacion_sistema
    )


@app.route("/transferencias")
def transferencias():
    return render_template(
        "transferencias.html",
        transferencias=transferencias_realizadas,
        informacion=informacion_sistema
    )


@app.route("/pagos")
def pagos():
    return render_template(
        "pagos.html",
        pagos=pagos_disponibles,
        informacion=informacion_sistema
    )


if __name__ == "__main__":
    app.run(debug=True)