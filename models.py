from flask_login import UserMixin
from conexion.conexion import obtener_conexion

class Usuario(UserMixin):
    def __init__(self, id, usuario, password):
        self.id = id
        self.usuario = usuario
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        res = cursor.fetchone()
        cursor.close()
        conexion.close()
        if res:
            return Usuario(id=res['id'], usuario=res['usuario'], password=res['password'])
        return None

    @staticmethod
    def get_by_username(username):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (username,))
        res = cursor.fetchone()
        cursor.close()
        conexion.close()
        if res:
            return Usuario(id=res['id'], usuario=res['usuario'], password=res['password'])
        return None