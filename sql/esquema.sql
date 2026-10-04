CREATE DATABASE IF NOT EXISTS BanGYE_Digital;
USE BanGYE_Digital;

-- 1. Tabla Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    cedula VARCHAR(10) NOT NULL UNIQUE,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT,
    fecha_nacimiento DATE,
    fecha_registro DATE DEFAULT (CURRENT_DATE)
);

-- 2. Tabla Cuentas Bancarias
CREATE TABLE IF NOT EXISTS cuentas_bancarias (
    id_cuenta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    numero_cuenta VARCHAR(10) NOT NULL UNIQUE,
    tipo_cuenta VARCHAR(50) NOT NULL,
    saldo_actual DECIMAL(10, 2) DEFAULT 0.00,
    fecha_apertura DATE DEFAULT (CURRENT_DATE),
    estado VARCHAR(20) NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE SET NULL
);

-- 3. Tabla Solicitudes
CREATE TABLE IF NOT EXISTS solicitudes (
    id_solicitud INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    nombre_solicitante VARCHAR(150) NOT NULL,
    correo_solicitante VARCHAR(100) NOT NULL,
    tipo_solicitud VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha_solicitud DATE DEFAULT (CURRENT_DATE),
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE SET NULL
);

-- 4. Tabla Pagos
CREATE TABLE IF NOT EXISTS pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_cuenta INT,
    monto DECIMAL(10, 2) NOT NULL,
    fecha_pago DATE DEFAULT (CURRENT_DATE),
    metodo_pago VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_cuenta) REFERENCES cuentas_bancarias(id_cuenta) ON DELETE SET NULL
);

-- 5. Tabla Transferencias
CREATE TABLE IF NOT EXISTS transferencias (
    id_transferencia INT AUTO_INCREMENT PRIMARY KEY,
    id_cuenta_origen INT,
    id_cuenta_destino INT,
    monto DECIMAL(10, 2) NOT NULL,
    fecha_transferencia DATE DEFAULT (CURRENT_DATE),
    estado VARCHAR(20) NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_cuenta_origen) REFERENCES cuentas_bancarias(id_cuenta) ON DELETE SET NULL,
    FOREIGN KEY (id_cuenta_destino) REFERENCES cuentas_bancarias(id_cuenta) ON DELETE SET NULL
);