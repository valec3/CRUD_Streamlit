import mysql.connector
def init_db():
    create_db()
    create_table()
    
def create_db():
    cnx = mysql.connector.connect(
            host = "localhost",
            user = "victor_stpy",
            password = "1234",
        )
    cursor = cnx.cursor()
    SQL_COMMAND = """
        CREATE DATABASE IF NOT EXISTS crud_stpy;
    """
    cursor.execute(SQL_COMMAND)
    cnx.commit()
    cnx.close()
    print("Base de datos creada exitosamente.")

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
    
def add_user(user):
    try:
        cnx = connect()
        cursor = cnx.cursor()
        SQL_COMMAND = """
            INSERT INTO USUARIOS (
                NOMBRE, 
                APELLIDO, 
                CORREO_ELECTRONICO, 
                NUMERO_DE_TELEFONO,
                CONTRASENA,
                FECHA_DE_REGISTRO 
            )
            VALUES (%s, %s, %s, %s, %s, NOW());
        """
        cursor.execute(SQL_COMMAND, user)
        print("Usuario agregado exitosamente.")
        return True
    except Exception as err:
        print("Error al agregar usuario: {}".format(err))
        return False
    finally:
        cnx.commit()
        cnx.close()

def read_usuarios():
    cnx = connect()
    cursor = cnx.cursor()
    SQL_COMMAND = """
        SELECT * FROM USUARIOS;
    """
    cursor.execute(SQL_COMMAND)
    usuarios = cursor.fetchall()
    cnx.close()
    return usuarios
def get_user(id):
    cnx = connect()
    cursor = cnx.cursor()
    SQL_COMMAND = """
        SELECT * FROM USUARIOS WHERE USER_ID = %s;
    """
    cursor.execute(SQL_COMMAND, (id,))
    user = cursor.fetchall()
    cnx.close()
    return user

def update_person(user):
    try:
        
        cnx = connect()
        cursor = cnx.cursor()
        SQL_COMMAND = """
            UPDATE USUARIOS SET 
                NOMBRE = %s, 
                APELLIDO = %s, 
                CORREO_ELECTRONICO = %s, 
                NUMERO_DE_TELEFONO = %s, 
                CONTRASENA = %s
            WHERE USER_ID = %s;
        """
        cursor.execute(SQL_COMMAND, user)
        cnx.commit()
        return True
    except Exception as err:
        print("Error al actualizar usuario: {}".format(err))
        return False
    finally:
        cnx.close()
    