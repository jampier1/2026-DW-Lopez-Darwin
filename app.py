import time
import mysql.connector
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Modelos
from models import Usuario

# Formularios
from forms.solicitud_form import SolicitudForm
from forms.cuenta_form import CuentaForm
from forms.transferencia_form import TransferenciaForm
from forms.pago_form import PagoForm
from forms.usuario_form import UsuarioForm
from forms.login_form import LoginForm

# Conexión
from conexion.conexion import obtener_conexion

app = Flask(__name__)

app.config["SECRET_KEY"] = "bangye-clave-segura-2026"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder a esta sección.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

informacion_sistema = {
    "nombre": "BanGYE Digital",
    "descripcion": "Sistema web de gestión de solicitudes y servicios financieros",
    "ciudad": "Guayaquil, Ecuador",
    "horario": "Lunes a Viernes de 8:00 AM a 17:00 PM"
}


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


@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html', informacion=informacion_sistema, servicios=servicios)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario_nom = form.usuario.data.strip()
        
        if Usuario.get_by_username(usuario_nom):
            flash('El nombre de usuario ya existe.', 'danger')
            return render_template('registro.html', form=form, informacion=informacion_sistema)

        # Cifrar contraseña requerida por la tarea (generate_password_hash)
        password_hashed = generate_password_hash(form.password.data)

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)"
            cursor.execute(sql, (usuario_nom, password_hashed))
            conexion.commit()
            flash('Usuario registrado exitosamente. Por favor inicia sesión.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            conexion.rollback()
            flash(f'Error al registrar en la base de datos: {err}', 'danger')
        finally:
            cursor.close()
            conexion.close()

    return render_template('registro.html', form=form, informacion=informacion_sistema)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        usuario_db = Usuario.get_by_username(form.usuario.data.strip())
        
        # Validación obligatoria con check_password_hash
        if usuario_db and check_password_hash(usuario_db.password, form.password.data):
            login_user(usuario_db)
            flash('Sesión iniciada correctamente.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html', form=form, informacion=informacion_sistema)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT COUNT(*) AS total FROM cuentas_bancarias")
        resultado = cursor.fetchone()
        total_cuentas = resultado['total'] if resultado else 0
    except mysql.connector.Error as err:
        print(f"Error al contar cuentas: {err}")
        total_cuentas = 0
    finally:
        cursor.close()
        conexion.close()

    solicitudes_pendientes = sum(1 for s in solicitudes_registradas if s.get('estado') == 'Pendiente')

    return render_template(
        'dashboard.html',
        total_cuentas=total_cuentas,
        solicitudes_pendientes=solicitudes_pendientes,
        informacion=informacion_sistema
    )

# ==========================================
# MÓDULO DE GESTIÓN DE CUENTAS BANCARIAS
# ==========================================

# 1. RUTA PRINCIPAL: LISTAR Y REGISTRAR CUENTAS (CREATE / READ)
@app.route('/cuentas', methods=['GET', 'POST'])
@login_required
def cuentas():
    form = CuentaForm()
    
    # AGREGAR NUEVA CUENTA (POST)
    if form.validate_on_submit():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        
        nombre_ingresado = form.titular.data.strip()
        
        # A) Buscar si el cliente ya existe
        sql_buscar_cliente = "SELECT id_cliente FROM clientes WHERE CONCAT(nombres, ' ', apellidos) LIKE %s OR nombres LIKE %s LIMIT 1"
        cursor.execute(sql_buscar_cliente, (f"%{nombre_ingresado}%", f"%{nombre_ingresado}%"))
        cliente_existente = cursor.fetchone()
        
        if cliente_existente:
            id_cliente = cliente_existente['id_cliente']
        else:
            # B) Si no existe, crearlo con cédula temporal ajustada a 10 caracteres máximo
            partes_nombre = nombre_ingresado.split(' ', 1)
            nombres = partes_nombre[0]
            apellidos = partes_nombre[1] if len(partes_nombre) > 1 else 'General'
            
            timestamp = str(int(time.time()))
            cedula_temp = f"C{timestamp}"[-10:]
            correo_temp = f"{nombres.lower()}_{timestamp}@ejemplo.com"
            fecha_nac_temp = "2000-01-01"

            sql_nuevo_cliente = """
                INSERT INTO clientes (cedula, nombres, apellidos, correo_electronico, fecha_nacimiento) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql_nuevo_cliente, (cedula_temp, nombres, apellidos, correo_temp, fecha_nac_temp))
            conexion.commit()
            id_cliente = cursor.lastrowid

        # C) Insertar la cuenta bancaria enlazada al id_cliente
        sql_insert_cuenta = """
            INSERT INTO cuentas_bancarias 
            (id_cliente, numero_cuenta, tipo_cuenta, saldo_actual, fecha_apertura, estado, descripcion)
            VALUES (%s, %s, %s, %s, CURDATE(), %s, %s)
        """
        valores = (
            id_cliente,
            form.numero.data,
            form.tipo.data,
            0.00,
            form.estado.data,
            form.descripcion.data
        )
        
        try:
            cursor.execute(sql_insert_cuenta, valores)
            conexion.commit()
        except mysql.connector.Error as err:
            conexion.rollback()
            print(f"Error al registrar la cuenta: {err}")
        finally:
            cursor.close()
            conexion.close()

        return redirect(url_for('cuentas'))

    # LISTAR CUENTAS REGISTRADAS (GET)
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    
    sql_select = """
        SELECT 
            cb.id_cuenta,
            cb.numero_cuenta,
            cb.tipo_cuenta,
            cb.descripcion,
            cb.fecha_apertura,
            cb.estado,
            CONCAT(c.nombres, ' ', c.apellidos) AS titular
        FROM cuentas_bancarias cb
        INNER JOIN clientes c ON cb.id_cliente = c.id_cliente
        ORDER BY cb.id_cuenta DESC
    """
    
    try:
        cursor.execute(sql_select)
        cuentas_bancarias = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error al consultar cuentas: {err}")
        cursor.execute("SELECT *, 'Sin Titular' AS titular FROM cuentas_bancarias ORDER BY id_cuenta DESC")
        cuentas_bancarias = cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()

    return render_template(
        "cuentas.html",
        cuentas=cuentas_bancarias,
        informacion=informacion_sistema,
        form=form
    )


# 2. RUTA PARA EDITAR CUENTA Y CLIENTE (UPDATE)
@app.route('/cuentas/editar/<int:id_cuenta>', methods=['GET', 'POST'])
@login_required
def editar_cuenta(id_cuenta):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT cb.*, c.id_cliente, CONCAT(c.nombres, ' ', c.apellidos) AS titular 
        FROM cuentas_bancarias cb 
        INNER JOIN clientes c ON cb.id_cliente = c.id_cliente 
        WHERE cb.id_cuenta = %s
    """, (id_cuenta,))
    cuenta = cursor.fetchone()
    
    if not cuenta:
        cursor.close()
        conexion.close()
        return redirect(url_for('cuentas'))
        
    form = CuentaForm(data={
        'titular': cuenta['titular'],
        'numero': cuenta['numero_cuenta'],
        'tipo': cuenta['tipo_cuenta'],
        'descripcion': cuenta['descripcion'],
        'estado': cuenta['estado']
    })

    if request.method == 'POST' and form.validate_on_submit():
        nombre_ingresado = form.titular.data.strip()
        partes_nombre = nombre_ingresado.split(' ', 1)
        nombres = partes_nombre[0]
        apellidos = partes_nombre[1] if len(partes_nombre) > 1 else ''

        try:
            # Actualizar nombres/apellidos del cliente
            sql_update_cliente = """
                UPDATE clientes 
                SET nombres = %s, apellidos = %s 
                WHERE id_cliente = %s
            """
            cursor.execute(sql_update_cliente, (nombres, apellidos, cuenta['id_cliente']))

            # Actualizar los datos de la cuenta
            sql_update_cuenta = """
                UPDATE cuentas_bancarias 
                SET numero_cuenta = %s, tipo_cuenta = %s, estado = %s, descripcion = %s
                WHERE id_cuenta = %s
            """
            cursor.execute(sql_update_cuenta, (
                form.numero.data,
                form.tipo.data,
                form.estado.data,
                form.descripcion.data,
                id_cuenta
            ))
            
            conexion.commit()
        except mysql.connector.Error as err:
            conexion.rollback()
            print(f"Error al actualizar datos: {err}")
        finally:
            cursor.close()
            conexion.close()

        return redirect(url_for('cuentas'))

    cursor.close()
    
    # Recargar lista de cuentas
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT cb.*, CONCAT(c.nombres, ' ', c.apellidos) AS titular 
        FROM cuentas_bancarias cb 
        INNER JOIN clientes c ON cb.id_cliente = c.id_cliente 
        ORDER BY cb.id_cuenta DESC
    """)
    cuentas_bancarias = cursor.fetchall()
    cursor.close()
    conexion.close()

    return render_template(
        'cuentas.html', 
        form=form, 
        cuentas=cuentas_bancarias, 
        informacion=informacion_sistema, 
        modo_edicion=True, 
        id_cuenta=id_cuenta
    )


# 3. RUTA PARA ELIMINAR CUENTA (DELETE)
@app.route('/cuentas/eliminar/<int:id_cuenta>', methods=['POST', 'GET'])
@login_required
def eliminar_cuenta(id_cuenta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("DELETE FROM cuentas_bancarias WHERE id_cuenta = %s", (id_cuenta,))
        conexion.commit()
    except mysql.connector.Error as err:
        conexion.rollback()
        print(f"Error al eliminar la cuenta: {err}")
    finally:
        cursor.close()
        conexion.close()
        
    return redirect(url_for('cuentas'))


@app.route("/transferencias", methods=["GET", "POST"])
@login_required
def transferencias():
    form = TransferenciaForm()
    if form.validate_on_submit():
        return redirect(url_for("transferencias"))

    return render_template(
        "transferencias.html",
        transferencias=transferencias_realizadas,
        informacion=informacion_sistema,
        form=form
    )

@app.route("/pagos", methods=["GET", "POST"])
@login_required
def pagos():
    form = PagoForm()
    if form.validate_on_submit():
        return redirect(url_for("pagos"))

    return render_template(
        "pagos.html",
        pagos=pagos_disponibles,
        informacion=informacion_sistema,
        form=form
    )

@app.route('/solicitudes', methods=['GET', 'POST'])
@login_required
def solicitudes():
    form = SolicitudForm()
    
    if form.validate_on_submit():
        # Lógica para procesar la nueva solicitud cuando envíen el formulario
        return redirect(url_for('solicitudes'))

    return render_template(
        'solicitudes.html',
        solicitudes=solicitudes_registradas,
        informacion=informacion_sistema,
        form=form
    )

if __name__ == "__main__":
    app.run(debug=True)