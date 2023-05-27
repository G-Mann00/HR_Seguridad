import pymysql

from datos.conexion import Conexion
from entidades.VwUserRol import VwUserRol

class Dt_tbl_UserRol:
    def __init__(self):
        pass
    _dbCon = Conexion()
    _con = None
    _cursor = None
    _sql = ""

    def listUsuarioRol(self):
        self._sql = "SELECT id_UserRol, id_user, id_rol FROM Seguridad.tbl_UserRol;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaUserRol = []

            for tur in registros:
                vwUR = VwUserRol()
                vwUR._idUserRol = tur['id_UserRol']
                vwUR._user = tur['id_user']
                vwUR._rol = tur['id_rol']
                listaUserRol.append(vwUR)
            print('listaUserRol', listaUserRol)
            return listaUserRol

        except Exception as e:
            print("Datos: Error listUsuarioRol()", e)
        finally:
            #self._dbCon.closeCon()
            pass
