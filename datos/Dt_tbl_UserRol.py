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
        self._sql = "SELECT * FROM VwUserRol;"
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
                vwUR._id_user = tur['id_user']
                vwUR._id_rol = tur['id_rol']
                vwUR._user = tur['user']
                vwUR._rol = tur['rol']
                listaUserRol.append(vwUR)
            print('listaUserRol', listaUserRol)
            return listaUserRol

        except Exception as e:
            print("Datos: Error listUsuarioRol()", e)
        finally:
            #self._dbCon.closeCon()
            pass

    #PENDIENTE
    def validarIdUnico(self, UserRol_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT country_id FROM Seguridad.countries WHERE country_id = '{country_param.country_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta de validarUnico de UserRol", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def actualizarUserRol(self, UserRol_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"UPDATE Seguridad.tbl_UserRol SET id_user = '{UserRol_param.id_user}', id_rol = '{UserRol_param.id_rol}' WHERE id_UserRol = '{UserRol_param._id_UserRol}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Error en la consulta en la actualizarUserRol", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
