import mysql.connector

# Creamos la conexión a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_g5"
)

print(f"Conexión exitosa a la base de datos: {connection.database}")

# SELECT

alumno_cursor = connection.cursor()
alumno_cursor.execute("SELECT * FROM alumno")
resultado = alumno_cursor.fetchall()
print(resultado)