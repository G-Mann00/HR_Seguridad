import pymysql

from datos.conexion import Conexion
from entidades.Tbl_rol import Tbl_rol
from entidades.VwRol import VwRol


class Dt_tbl_rol:
    def __init__(self):
        self._con = None
        self._cursor = None

    def listarRol(self):
        listaRol = []
        try:

            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = "SELECT * FROM Seguridad.VwRolEstado where estado <> 3;"
            self._cursor.execute(sql)

            registros = self._cursor.fetchall()
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
            Conexion.closeCursor()
            Conexion.closeConnection()

    def agregarRol(self, rol_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"INSERT INTO Seguridad.tbl_rol (rol, estado) values ('{rol_param.rol}', {rol_param.estado});"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error al insertar rol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarRol(self, rol_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.tbl_rol SET estado = 3 where id_rol = {rol_param.id_rol};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error al eliminar rol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def buscarRol(self, rol_param):
        listaRol = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f" SELECT * from Seguridad.VwRolEstado where rol like '%{rol_param.rol}%' and estado <> 3;"

            resultados = cursor.execute(sql)
            print(f"Resultados: {resultados}")

            registros = cursor.fetchall()
            for r in registros:
                id = r['id_rol']
                nombre = r['rol']
                vista = VwRol(id, nombre)
                listaRol.append(vista)
        except Exception as e:
            print(f"Error en la busqueda: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaRol

    def editarRol(self, rol_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.tbl_rol SET rol = '{rol_param.rol}' where id_rol = {rol_param.id_rol};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error al editar rol {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

