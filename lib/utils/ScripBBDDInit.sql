CREATE DATABASE IF NOT EXISTS HorariosAPP;

-- Seleccionar la base de datos que acabamos de crear
USE HorariosAPP;

-- Crear tabla Equipos
CREATE TABLE IF NOT EXISTS Equipos (
    id_equipo INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    horas_inicio_act TIME,
    hora_fin_act TIME
) ENGINE=InnoDB;

-- Crear tabla Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('Trabajador', 'Jefe', 'Admin') NOT NULL,
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


-- Insertar datos en la tabla Equipos
INSERT INTO Equipos (tipo, nombre, horas_inicio_act, hora_fin_act) 
VALUES 
('Desarrollo', 'Equipo A', '08:00:00', '16:00:00'),
('Marketing', 'Equipo B', '09:00:00', '17:00:00'),
('Soporte', 'Equipo C', '10:00:00', '18:00:00'),
('Ventas', 'Equipo D', '07:00:00', '15:00:00'),
('Finanzas', 'Equipo E', '08:30:00', '16:30:00'),
('Legal', 'Equipo F', '09:00:00', '17:00:00');

-- Insertar datos en la tabla Usuario
INSERT INTO Usuario (tipo, nombre, email, contrasena, id_equipo) 
VALUES 
('Admin', 'Carlos Pérez', 'carlos.perez@example.com', 'password123', 1),
('Trabajador', 'Ana Gómez', 'ana.gomez@example.com', 'pass456', 2),
('Trabajador', 'Luis Torres', 'luis.torres@example.com', 'secret789', 1),
('Trabajador', 'María Sánchez', 'maria.sanchez@example.com', 'pass321', 3),
('Admin', 'Raúl Ortega', 'raul.ortega@example.com', 'password456', 4),
('Trabajador', 'Sofía Navarro', 'sofia.navarro@example.com', 'mypassword123', 2),
('Trabajador', 'Javier Ruiz', 'javier.ruiz@example.com', 'secure456', 5),
('Trabajador', 'Elena Martínez', 'elena.martinez@example.com', 'secretpass', 6),
('Trabajador', 'Ricardo López', 'ricardo.lopez@example.com', 'topsecret789', 3),
('Trabajador', 'Natalia Vargas', 'natalia.vargas@example.com', 'vargas456', 4);

-- Insertar datos en la tabla Horarios
INSERT INTO Horarios (id_usuario, fecha, hora_inicio, hora_fin) 
VALUES 
(1, '2024-10-30', '08:00:00', '16:00:00'),
(2, '2024-10-30', '09:00:00', '17:00:00'),
(3, '2024-10-31', '10:00:00', '18:00:00'),
(4, '2024-11-01', '07:00:00', '15:00:00'),
(1, '2024-11-02', '08:00:00', '12:00:00'),
(5, '2024-11-02', '09:00:00', '17:00:00'),
(6, '2024-11-03', '10:00:00', '16:00:00'),
(7, '2024-11-03', '08:30:00', '17:30:00'),
(8, '2024-11-04', '09:00:00', '18:00:00'),
(9, '2024-11-04', '07:30:00', '16:30:00'),
(10, '2024-11-05', '08:00:00', '15:00:00'),
(1, '2024-11-05', '08:00:00', '14:00:00'),
(2, '2024-11-06', '08:30:00', '15:30:00'),
(3, '2024-11-06', '09:00:00', '17:00:00'),
(4, '2024-11-07', '07:30:00', '14:30:00'),
(5, '2024-11-07', '09:00:00', '17:00:00'),
(6, '2024-11-08', '10:00:00', '16:00:00'),
(7, '2024-11-08', '08:00:00', '15:00:00'),
(8, '2024-11-09', '07:00:00', '15:00:00'),
(9, '2024-11-09', '09:00:00', '17:00:00');
