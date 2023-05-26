from datos.conexion import Conexion
from entidades.Region import Region
from datos.conexion import Conexion


class Dt_Region:
    _con = None
    _cursor = None

    def __init__(self):
        pass


    def listarRegion(self):
        listaRegion = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = "SELECT * FROM Seguridad.regions;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['region_id']
                nombre = r['region_name']
                region = Region(id, nombre)
                listaRegion.append(region)
            return listaRegion
        except Exception as e:
            print("Datos: Error listarRegion", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def filtrarRegion(self, region_param):
        listaRegion = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"SELECT * FROM Seguridad.regions WHERE region_name LIKE '%{region_param.region_name}%';"
            num= self._cursor.execute(sql)
            print(f"Hola soy el resultado del executre : {num}")
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['region_id']
                nombre = r['region_name']
                region = Region(id, nombre)
                listaRegion.append(region)
            return listaRegion

        except Exception as e:
            print("Datos: Error en listaRegion()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def insertarRegion(self, region_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"INSERT INTO Seguridad.regions(region_name) VALUES ('{region_param.region_name}');"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en insertarRegion() {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def actualizarRegion(self, region_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.regions SET region_name = '{region_param.region_name}' WHERE region_id = {region_param.region_id};"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en actualizarRegion() {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def eliminarRegion(self, region_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.regions WHERE region_id = {region_param.region_id};"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado

        except Exception as e:
            print(f"Datos: Error en eliminarRegion() {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    # Retorta True si existe esa región
    def existeRegion(self, region_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = Conexion.getCursor()
            sql = f"SELECT * FROM Seguridad.regions WHERE region_name = '{region_param.region_name}';"
            self._cursor.execute(sql)
            if self._cursor.rowcount > 0:
                resultado = True

            return resultado

        except Exception as e:
            print(f"Datos: Error en ExisteRegion() {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

