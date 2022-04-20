import sqlite3
from src.imp.base.database import AbstactClassDB


class database(AbstactClassDB):
    def __init__(self):
        self.version_SQLite()
        self.crear_tablas()
        # creai y coneccion
        pass

    def save_list(self, lisofchannels, bool):
        pass

    def get_list(self, bool):
        pass

    def version_SQLite(self):
        try:
            conexion = sqlite3.connect('api_twitch.db')
            cursor = conexion.cursor()
            #print('Conectado a SQLite')

            query = 'SELECT sqlite_version();'
            cursor.execute(query)
            row = cursor.fetchall()
            #print('Version de SQLite: ', row)
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexion', error)
        finally:
            if(conexion):
                conexion.close()
                #print('Conexion a SQLite cerrada\n')

    def crear_tablas(self):
        # TablaUSUARIOS
        try:
            conexion = sqlite3.connect('api_twitch.db')
            cursor = conexion.cursor()
            #print('Conectado a SQLite')

            query = '''
                CREATE TABLE IF NOT EXISTS seguidos(
                    id_usuario INTEGER PRIMARY KEY ,
                    nombre_usuario TEXT,
                    ponderacion float,
                    bloqueado boolean,
                    recomendado boolean
                );
            '''
            cursor.execute(query)
            row = cursor.fetchall()
            #print('Tabla creada correctamente', row)
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexion', error)
        finally:
            if(conexion):
                conexion.close()
                #print('Conexion a SQLite cerrada\n')

    def agregar_usuario(self, id_usuario, nombre_usuaio, ponderacion, bloqueado, recomendado):
        try:
            conexion = sqlite3.connect('api_twitch.db')
            cursor = conexion.cursor()
            # print('Conectado')

            query = """INSERT INTO seguidos VALUES
                    ({}, '{}', '{}', '{}','{}',{})""".format(id_usuario, nombre_usuaio, ponderacion, bloqueado, recomendado)
            resultado = cursor.execute(query)
            conexion.commit()
            #print('Valor Insertado Correctamente', resultado)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion', error)

        finally:
            if(conexion):
                conexion.close()

    def mostrar_usuario(self):
        try:
            conexion = sqlite3.connect('api_twitch.db')
            cursor = conexion.cursor()
            # print('Conectado')

            query = """SELECT * FROM seguidos"""
            resultado = cursor.execute(query)
            conexion.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print('Error con la conexion', error)

        finally:
            if(conexion):
                conexion.close()

    def eliminar_usuario(self, id_usuario):
        try:
            conexion = sqlite3.connect('api_twitch.db')
            cursor = conexion.cursor()
            # print('Conectado')

            query = "DELETE FROM seguidos WHERE id_name = {}".format(
                id_usuario)
            resultado = cursor.execute(query)
            conexion.commit()
            #print('Valor Eliminado Correctamente', resultado)
            cursor.close()
        except sqlite3.Error as error:
            print('Error con la conexion', error)
        finally:
            if(conexion):
                conexion.close()
