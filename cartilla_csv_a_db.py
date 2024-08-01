import sqlite3
import csv
import os

# Ruta al archivo CSV
csv_file = '/Users/praguirre/osvimed_digital/cartilla_CABA_con_especialidad.csv'

# Nombre del archivo de base de datos SQLite
db_file = 'cartilla_medica_caba.db'

# Verificar si el archivo CSV existe
if not os.path.exists(csv_file):
    print(f"El archivo {csv_file} no existe. Por favor verifica la ruta.")
else:
    # Crear la conexión a la base de datos
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Crear la tabla en la base de datos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Profesionales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Profesional TEXT,
        Direccion TEXT,
        Telefono TEXT,
        Mail TEXT,
        Especialidad TEXT
    )
    ''')

    # Abrir y leer el archivo CSV
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
            INSERT INTO Profesionales (Profesional, Direccion, Telefono, Mail, Especialidad)
            VALUES (?, ?, ?, ?, ?)
            ''', (row['Profesional'], row['Direccion'], row['Telefono'], row['Mail'], row['Especialidad']))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print(f"Los datos del archivo {csv_file} se han transferido a la base de datos {db_file}.")
