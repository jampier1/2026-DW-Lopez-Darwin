import os
import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "12345"),
        database=os.getenv("MYSQL_DATABASE", "BanGYE_Digital"),
        port=int(os.getenv("MYSQL_PORT", 3306))
    )
    return conexion