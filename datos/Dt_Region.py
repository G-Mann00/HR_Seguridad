from datos.conexion import Conexion
from entidades.Region import Region
from datos.conexion import Conexion


class Dt_Region:

    def __init__(self):
        self._con = None
        self._cursor = None
        #self._cursor = Conexion.getCursor()

    def listarRegion(self):
        listaRegion = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = "SELECT * FROM Seguridad.regions;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['region_id']
                nombre = r['region_name']
                region = Region(id, nombre)
                listaRegion.append(region)
            self._cursor.close()
            return listaRegion
        except Exception as e:
            print("Error en la consulta", e)
            if self._con.open:
                self._con.close()
                self._cursor.close()
                print("MySQL connection was closed")

    def buscarRegion(self, Region_param):
        listaRegion = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()

            sql = f"SELECT * FROM Seguridad.regions WHERE region_name LIKE '%{Region_param.region_name}%';"
            self._cursor.execute(sql)

            registros = self._cursor.fetchall()
            for r in registros:
                id = r['region_id']
                nombre = r['region_name']
                region = Region(id, nombre)
                listaRegion.append(region)
                print(f"Region: {region}")
            self._cursor.close()
            return listaRegion
        except Exception as e:
            print("Error en la consulta", e)
            if self._con.open:
                self._con.close()
                self._cursor.close()
                print("MySQL connection was closed")

    def buscar(self, region_param):
        listaRegion = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            print(con.open)
            if cursor:
                print("Estoy abierto")
            else:
                print("Estoy cerrado")
            sql = f"SELECT * FROM Seguridad.regions WHERE region_name LIKE '%{region_param.region_name}%';"
            num= cursor.execute(sql)
            print(f"Hola soy el resultado del executre : {num}")
            registros = cursor.fetchall()
            for r in registros:
                id = r['region_id']
                nombre = r['region_name']
                region = Region(id, nombre)
                listaRegion.append(region)
                print(f"Region: {region}")
            return listaRegion
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def insertarRegion(self, region_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"INSERT INTO Seguridad.regions(region_name) VALUES ('{region_param.region_name}');"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la insercion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def actualizarRegion(self, region_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.regions SET region_name = '{region_param.region_name}' WHERE region_id = {region_param.region_id};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la actualizacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarRegion(self, region_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.regions WHERE region_id = {region_param.region_id};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la eliminacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
