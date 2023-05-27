from datos.conexion import Conexion
from entidades.Location import Location
from entidades.VwLocations import VwLocations

class Dt_Location:
    con = None
    cursor = None


    def __init__(self):
        pass

    def agregarLocation(self, Location_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = "INSERT INTO Seguridad.locations (street_address, postal_code, city, state_province, country_id) " \
                  "VALUES (%s, %s, %s, %s, %s);"
            values = (
                Location_param.street_address,
                Location_param.postal_code,
                Location_param.city,
                Location_param.state_province,
                Location_param.country_id
            )
            if self._cursor.execute(sql, values) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado


    def listarLocations(self):
        listaLocations = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql ="SELECT * FROM Seguridad.VwLocations;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['location_id']
                street_address = r['street_address']
                postal_code = r['postal_code']
                city = r['city']
                state_province = r['state_province']
                country_name = r['country_name']
                vistas = VwLocations(id, country_name,state_province, city, postal_code, street_address)
                listaLocations.append(vistas)
            return listaLocations
        except Exception as e:
            print("Datos: Error en listarLocations()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def actualizarLocation(self, location_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"UPDATE Seguridad.locations SET street_address = '{location_param.street_address}'" \
                  f", postal_code = '{location_param.postal_code}'" \
                  f", city = '{location_param.city}'" \
                  f", state_province = '{location_param.state_province}'" \
                  f", country_id = '{location_param.country_id}'" \
                  f" WHERE location_id = {location_param.location_id};"

            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

            return resultado
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def eliminarLocation(self, location_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"DELETE FROM Seguridad.locations WHERE location_id = {location_param.location_id};"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()
            return resultado
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarPorPais(self, cadena):
        listaLocations = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT * FROM Seguridad.VwLocations WHERE country_name like '%{cadena}%';"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['location_id']
                street_address = r['street_address']
                postal_code = r['postal_code']
                city = r['city']
                state_province = r['state_province']
                country_name = r['country_name']
                vistas = VwLocations(id, country_name, state_province, city, postal_code, street_address)
                listaLocations.append(vistas)
            return listaLocations
        except Exception as e:
            print("Datos: Error en buscarPorPais()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarPorCiudad(self, cadena):
        listaLocations = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT * FROM Seguridad.VwLocations WHERE city like '%{cadena}%';"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['location_id']
                street_address = r['street_address']
                postal_code = r['postal_code']
                city = r['city']
                state_province = r['state_province']
                country_name = r['country_name']
                vistas = VwLocations(id, country_name, state_province, city, postal_code, street_address)
                listaLocations.append(vistas)
            return listaLocations
        except Exception as e:
            print("Datos: Error en buscarPorCiudad()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()




