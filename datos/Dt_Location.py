from datos.conexion import Conexion
from entidades.Location import Location


class Dt_Location:

    def __init__(self):
        self._con = None
        self._cursor = None

    #Funcion que nos permite validar si un campo viene "" para cambiarlo por NULL. Si no ese hace esto, los datos se guardaran como ""
    def comprobarNull(self, location_param):
        if location_param.street_address == "":
            location_param.street_address = None
        if location_param.postal_code == "":
            location_param.postal_code = None
        if location_param.state_province == "":
            location_param.state_province = None
        return location_param


    # def agregarLocation(self,Location_param):
    #     resultado = False
    #     try:
    #         location_param = self.comprobarNull(Location_param)
    #         self._con = Conexion.getConnection()
    #         self._cursor = self._con.cursor()
    #         sql = f"INSERT INTO Seguridad.locations (street_address, postal_code, city, state_province, country_id) " \
    #               f"VALUES ('{Location_param.street_address}', '{Location_param.postal_code}', '{Location_param.city}','{Location_param.state_province}', '{Location_param.country_id}');"
    #         if self._cursor.execute(sql) > 0:
    #             resultado = True
    #         self._con.commit()
    #
    #     except Exception as e:
    #         print("Error en la consulta", e)
    #     finally:
    #         Conexion.closeCursor()
    #         Conexion.closeConnection()
    #         return resultado

    def agregarLocation(self, Location_param):
        resultado = False
        try:
            location_param = self.comprobarNull(Location_param)
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
            sql ="SELECT l.location_id, c.country_name, l.state_province, l.city, l.postal_code, l.street_address from Seguridad.locations as l inner join Seguridad.countries as c on l.country_id = c.country_id;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['location_id']
                street_address = r['street_address']
                postal_code = r['postal_code']
                city = r['city']
                state_province = r['state_province']
                #country_id = r['country_id']
                country_name = r['country_name']
                location = Location(id, street_address, postal_code, city, state_province, country_name)
                listaLocations.append(location)
            return listaLocations
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()




