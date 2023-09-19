import mysql.connector

def connect():
    """ Connect to MySQL database """
    cnx = None
    try:
        cnx = mysql.connector.connect(
            host = "localhost",
            user = "victor_stpy",
            password = "1234",
            database = "crud_stpy"
        )
        if cnx.is_connected():
            print("Conexión exitosa a la base de datos.")
        else:
            print("No se pudo conectar a la base de datos.")
        return cnx
    
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos: {}".format(err))
        return None
        
def create_table():
    cnx = connect()
    cursor = cnx.cursor()
    SQL_COMMAND = """
        CREATE TABLE IF NOT EXISTS USUARIOS (
        USER_ID INT AUTO_INCREMENT PRIMARY KEY,
        NOMBRE VARCHAR(50) NOT NULL,
        APELLIDO VARCHAR(50) NOT NULL,
        CORREO_ELECTRONICO VARCHAR(100) NOT NULL UNIQUE,
        CONTRASENA VARCHAR(50) NOT NULL,
        FECHA_DE_REGISTRO DATE NOT NULL,
        NUMERO_DE_TELEFONO VARCHAR(20)
        );
    """
    cursor.execute(SQL_COMMAND)
    cnx.commit()
    cnx.close()
    print("Tabla creada exitosamente.")
    

