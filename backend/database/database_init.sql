-- Tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

-- Tabla de empleados
CREATE TABLE IF NOT EXISTS  empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(50),
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    fecha_contratacion DATE DEFAULT CURRENT_DATE
);

-- Insertar 3 empleados
INSERT INTO empleados (nombre, puesto, correo, telefono) VALUES
('María González', 'Peluquera', 'maria@peluqueria.com', '600123456'),
('Carlos Pérez', 'Peluquero', 'carlos@peluqueria.com', '600654321'),
('Laura Ramírez', 'Colorista', 'laura@peluqueria.com', '600987654');

-- Tabla de servicios
CREATE TABLE IF NOT EXISTS servicios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(8,2) NOT NULL,
    duracion_minutos INT NOT NULL
);

-- Insertar 5 servicios
INSERT INTO servicios (nombre, descripcion, precio, duracion_minutos) VALUES
('Corte de cabello', 'Corte clásico y moderno para hombre y mujer', 15.00, 30),
('Peinado', 'Peinados para eventos y ocasiones especiales', 25.00, 45),
('Coloración', 'Cambio de color o retoque de raíces', 40.00, 90),
('Alisado', 'Alisado profesional para todo tipo de cabello', 60.00, 120),
('Tratamiento capilar', 'Tratamientos nutritivos y reparadores', 35.00, 60);


-- Tabla de reservas
CREATE TABLE IF NOT EXISTS reservas (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    empleado_id INT NOT NULL,
    servicio_id INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    hora_reserva TIME NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    FOREIGN KEY (servicio_id) REFERENCES servicios(id)
);

-- Índices
CREATE INDEX idx_reservas_fecha ON reservas(fecha_reserva);
CREATE INDEX idx_reservas_cliente ON reservas(cliente_id);
