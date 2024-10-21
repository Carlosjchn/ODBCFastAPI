-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS HorariosAPP;

-- Seleccionar la base de datos que acabamos de crear
USE HorariosAPP;

-- Crear tabla Equipos
CREATE TABLE IF NOT EXISTS Equipos (
    id_equipo INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('Normal', 'Jefe', 'Admin') NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    horas_inicio_act TIME,
    hora_fin_act TIME
) ENGINE=InnoDB;

-- Crear tabla Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('Normal', 'Jefe', 'Admin') NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    id_equipo INT,
    FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Crear tabla Horarios
CREATE TABLE IF NOT EXISTS Horarios (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insertar datos de ejemplo en la tabla Equipos
INSERT INTO Equipos (tipo, nombre) VALUES
  ('Normal', 'Equipo de Desarrollo'),
  ('Jefe', 'Equipo de Gestión'),
  ('Admin', 'Equipo de Administración');

-- Obtener los IDs de los equipos insertados
SET @equipo_desarrollo = LAST_INSERT_ID();
SET @equipo_gestion = LAST_INSERT_ID();
SET @equipo_administracion = LAST_INSERT_ID();

-- Insertar datos de ejemplo en la tabla Usuario
INSERT INTO Usuario (tipo, nombre, email, contrasena, id_equipo) VALUES
  ('Normal', 'Juan Pérez', 'juan@example.com', 'contraseña123', @equipo_desarrollo),
  ('Jefe', 'María López', 'maria@example.com', 'contraseña456', @equipo_gestion),
  ('Admin', 'Pedro Gómez', 'pedro@example.com', 'contraseña789', @equipo_administracion);

-- Insertar datos de ejemplo en la tabla Horarios
INSERT INTO Horarios (id_usuario, fecha, hora_inicio, hora_fin) VALUES
  (LAST_INSERT_ID(), '2023-11-20', '09:00:00', '17:00:00'),
  (LAST_INSERT_ID(), '2023-11-21', '08:00:00', '16:00:00'),
  (LAST_INSERT_ID(), '2023-11-22', '10:00:00', '18:00:00');