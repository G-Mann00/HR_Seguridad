import pymysql

from datos.conexion import Conexion
from entidades.Tbl_rol import Tbl_rol
from entidades.VwRol import VwRol


class Dt_tbl_rol:
    def __init__(self):
        pass
    _dbCon = Conexion()
    _con = None
    _cursor = None
    _sql = ""

    def llenarCbxRol(self):
        self._sql = "SELECT id_rol, rol FROM Seguridad.tbl_rol where estado<>3;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaRol = []

            for tr in registros:
                trol = Tbl_rol(tr['id_rol'], tr['rol'])
                listaRol.append(trol)
            print('listaRol', listaRol)
            return listaRol

        except Exception as e:
            print("Datos: Error llenarCbxRol()", e)
        finally:
            #self._dbCon.closeConnection()
            pass

    def listarRol(self):
        self._sql = "SELECT * FROM Seguridad.VwRol;"
        try:

            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            self._cursor.execute(self._sql)

            registros = self._cursor.fetchall()
            listaRol = []
            for r in registros:
                id = r['id_rol']
                nombre = r['rol']
                rol = VwRol(id, nombre)
                listaRol.append(rol)
            self._cursor.close()
            return listaRol

        except Exception as e:
            print("Datos: Error en listarRol", e)

        finally:
            self._dbCon.closeConnection()
            pass
