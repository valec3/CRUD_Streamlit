import mysql.connector

# Configuracion para conectar a la base de datos de Railway
CONFIG_MYSQL_DATABASE = {
    'user': 'root',
    'host': 'containers-us-west-53.railway.app',
    'password': 'efbah3sHqS7v52nna7ln',
    'database': 'railway',
    'port': 5557
}


def init_db():
    create_db()
    create_table()
    
def create_db():
    cnx = mysql.connector.connect(
            host = CONFIG_MYSQL_DATABASE['host'],
            user = CONFIG_MYSQL_DATABASE['user'],
            password = CONFIG_MYSQL_DATABASE['password'],
            database = CONFIG_MYSQL_DATABASE['database'],
            port = CONFIG_MYSQL_DATABASE['port']
        )
    cursor = cnx.cursor()
    SQL_COMMAND = """
        CREATE DATABASE IF NOT EXISTS railway;
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
            host = CONFIG_MYSQL_DATABASE['host'],
            user = CONFIG_MYSQL_DATABASE['user'],
            password = CONFIG_MYSQL_DATABASE['password'],
            database = CONFIG_MYSQL_DATABASE['database'],
            port = CONFIG_MYSQL_DATABASE['port']
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
    
def delete_user(id):
    try:
        
        cnx = connect()
        cursor = cnx.cursor()
        SQL_COMMAND = """
            DELETE FROM USUARIOS WHERE USER_ID = %s;
        """
        cursor.execute(SQL_COMMAND, (id,))
        cnx.commit()
        return True
    except Exception as e:
        print("Error al eliminar usuario: {}".format(e))
        return False
    finally:
        cnx.close()
    