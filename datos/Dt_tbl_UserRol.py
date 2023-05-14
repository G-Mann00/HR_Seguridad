import pymysql

from datos.conexion import Conexion
from entidades.Tbl_UserRol import Tbl_UserRol

class Dt_tbl_UserRol:
    def __init__(self):
        super().__init__()
    _con = Conexion.getConnection()
    _cursor = Conexion.getCursor()
    #_cursor = _con.cursor()
    _sql = ""

    def listUserRol(self):
        self._sql = "SELECT * FROM Seguridad.tbl_UserRol;"
        try:
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaUserRol = []

            for tu in registros:
                tus = Tbl_UserRol(tu['id_UserRol'], tu['id_user'], tu['id_rol'])
                listaUserRol.append(tus)
            print('listaUserRol[]', listaUserRol)
            return listaUserRol

        except Exception as e:
            print("Datos: Error listaUserRol()", e)
        finally:
            if self._con.open:
                self._con.close()
                self._cursor.close()
                print("MySQL connection was closed")
