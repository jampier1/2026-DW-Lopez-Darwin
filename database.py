import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "bangye.db")


def obtener_conexion():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_bd():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuentas (
            numero TEXT PRIMARY KEY,
            titular TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM cuentas")
    total_registros = cursor.fetchone()[0]

    if total_registros == 0:
        datos_iniciales = [
            ("001-000123", "María González", "Cuenta de Ahorros",
             "Cuenta destinada al ahorro y administración de fondos.", "05/06/2026", "Activa"),
            ("001-000456", "Carlos Mendoza", "Cuenta Corriente",
             "Cuenta para gestionar operaciones y movimientos financieros.", "21/06/2026", "Activa"),
            ("001-000789", "Andrea López", "Cuenta Corriente",
             "Cuenta para gestionar operaciones y movimientos financieros.", "10/07/2026", "Pendiente"),
            ("001-000812", "José Ramírez", "Cuenta de Ahorros",
             "Cuenta destinada al ahorro y administración de fondos.", "28/07/2026", "Activa"),
        ]
        cursor.executemany(
            "INSERT INTO cuentas (numero, titular, tipo, descripcion, fecha, estado) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            datos_iniciales
        )
        conn.commit()

    conn.close()


def obtener_cuentas():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT numero, titular, tipo, descripcion, fecha, estado FROM cuentas"
    )
    filas = cursor.fetchall()
    conn.close()

    cuentas = []
    for fila in filas:
        cuentas.append({
            "numero": fila["numero"],
            "titular": fila["titular"],
            "tipo": fila["tipo"],
            "descripcion": fila["descripcion"],
            "fecha": fila["fecha"],
            "estado": fila["estado"]
        })
    return cuentas


def insertar_cuenta(numero, titular, tipo, descripcion, fecha, estado):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cuentas (numero, titular, tipo, descripcion, fecha, estado) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (numero, titular, tipo, descripcion, fecha, estado)
    )
    conn.commit()
    conn.close()