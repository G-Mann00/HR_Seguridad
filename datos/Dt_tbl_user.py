import pymysql

from datos.conexion import Conexion
from entidades.Tbl_user import tbl_user


class Dt_tbl_user:
    def __init__(self):
        pass
    _dbCon = Conexion()
    _con = None
    _cursor = None
    #_cursor = _con.cursor()
    _sql = ""
    _result = None

    def listUsuarios(self):
        self._sql = "SELECT * FROM Seguridad.tbl_user where estado<>3;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaUsuario = []

            for tu in registros:
                tus = tbl_user(tu['id_user'], tu['user'], tu['pwd'], tu['nombres'],
                            tu['apellidos'], tu['email'], tu['pwd_temp'], tu['estado'])
                listaUsuario.append(tus)
            print('listaUsuario[]', listaUsuario)
            return listaUsuario

        except Exception as e:
            print("Datos: Error listUsuarios()", e)
        finally:
            #self._dbCon.closeCon()
            pass

    def insertUsuario(self, Tbl_user):
        self._sql = '''INSERT INTO Seguridad.tbl_user 
        (user, pwd, nombres, apellidos, email, pwd_temp, estado) 
        VALUES ('{}','{}','{}','{}','{}','{}','{}');'''.format(Tbl_user._user, Tbl_user._pwd, Tbl_user._nombres, Tbl_user._apellidos, Tbl_user._email, Tbl_user._pwd_temp, Tbl_user._estado)
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            self._con.commit()
            _result = 1
            return _result
        except Exception as e:
            print("Datos: Error insertUsuario()", e)
        finally:
            #self._dbCon.closeCon()
            pass

    def llenarCbxUser(self):
        self._sql = "SELECT id_user, user FROM Seguridad.tbl_user Where estado<>3;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaUsuario = []

            for tu in registros:
                tus = tbl_user(tu['id_user'], tu['user'])
                listaUsuario.append(tus)
            print('listaUsuario', listaUsuario)
            return listaUsuario

        except Exception as e:
            print("Datos: Error llenarCbxUser()", e)
        finally:
            #self._dbCon.closeCon()
            pass

    def existeUser(self, userName):

        self._sql = '''SELECT user FROM Seguridad.tbl_user where estado <>3 and user = '{}';'''.format(userName)
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            if(self._cursor.rowcount>0):
                return True
            else:
                return False
        except Exception as e:
            print("Datos: Error existeUser()", e)
        finally:
            #self._dbCon.closeConnection()
            pass
