import mariadb


def initialize_database(cursor):
    try:
        # Crear la base de datos
        cursor.execute("CREATE DATABASE IF NOT EXISTS HorariosAPP")
        cursor.execute("USE HorariosAPP")

        # Crear tabla Equipos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Equipos (
                id_equipo INT AUTO_INCREMENT PRIMARY KEY,
                tipo ENUM('Normal', 'Jefe', 'Admin') NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                horas_activos TIME
            )
        ''')

        # Crear tabla Usuario
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuario (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                tipo ENUM('Normal', 'Jefe', 'Admin') NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                contrasena VARCHAR(255) NOT NULL,
                id_equipo INT,
                FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo) ON DELETE SET NULL
            )
        ''')

        # Crear tabla Horarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Horarios (
                id_horario INT AUTO_INCREMENT PRIMARY KEY,
                id_usuario INT,
                fecha DATE NOT NULL,
                hora_inicio TIME NOT NULL,
                hora_fin TIME NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
            )
        ''')
        print("Tablas creadas con éxito.")
    except mariadb.Error as e:
        print(f"Error al crear las tablas: {e}")