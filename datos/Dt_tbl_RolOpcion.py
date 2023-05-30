import pymysql

from datos.conexion import Conexion
from entidades.VwRolOpcion import VwRolOpcion

class Dt_tbl_RolOpcion:
    def __init__(self):
        pass
    _dbCon = Conexion()
    _con = None
    _cursor = None
    _sql = ""

    def listRolOpcion(self):
        self._sql = "SELECT * FROM VwRolOpcion;"
        try:
            # abrimos la conexion & cursor
            self._con = self._dbCon.getConnection()
            self._cursor = self._dbCon.getCursor()
            # ejecutamos la consulta
            self._cursor.execute(self._sql)
            # Obtenemos todos los registros de la consulta
            registros = self._cursor.fetchall()
            print("Numero total de registros: ", self._cursor.rowcount)
            listaRolOpcion = []

            for tur in registros:
                vwUR = VwRolOpcion()
                vwUR._id_RolOpcion = tur['id_rolOpcion']
                vwUR._id_rol = tur['id_rol']
                vwUR._id_opcion = tur['id_opcion']
                vwUR._rol = tur['rol']
                vwUR._opcion = tur['opcion']
                listaRolOpcion.append(vwUR)
            print('listaRolOpcion', listaRolOpcion)
            return listaRolOpcion

        except Exception as e:
            print("Datos: Error listRolOpcion()", e)
        finally:
            #self._dbCon.closeCon()
            pass

    def insertarRolOpcion(self, RolOpcion_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"INSERT INTO Seguridad.tbl_rolOpcion ( id_rol, id_opcion)" \
                  f"VALUES ('{RolOpcion_param.id_rol}', {RolOpcion_param.id_opcion});"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Error en la consulta en la InsertarRolOpcion", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarRolOpcion(self, RolOpcion_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.tbl_rolOpcion WHERE id_rolOpcion = '{RolOpcion_param.id_RolOpcion}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la eliminacion de RolOpcion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def validarIdUnico(self, RolOpcion_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT tbl_UserRol FROM Seguridad.tbl_UserRol WHERE id_UserRol = '{RolOpcion_param.id_UserRol}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta validarIdUnico", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
