from datos.conexion import Conexion
from entidades.Country import Country

class Dt_Country:

    def __init__(self):
        self._con = None
        self._cursor = None

    def listarPaises(self):
        listaPaises = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql ="SELECT c.country_id, c.country_name, r.region_name from Seguridad.countries as c inner join Seguridad.regions as r on c.region_id = r.region_id;"

            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['country_id']
                nombre = r['country_name']
                region_name = r['region_name']
                pais = Country(id, nombre, region_name) #No me gusta. Estamos creando un objeto Country con un atributo que no le corresponde
                listaPaises.append(pais)
            return listaPaises
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


    def insertarPais(self, pais_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"INSERT INTO Seguridad.countries (country_id, country_name, region_id) " \
                  f"VALUES ('{pais_param.country_id}', '{pais_param.country_name}', {pais_param.region_id});"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def validarIdUnico(self, country_id):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT country_id FROM Seguridad.countries WHERE country_id = '{country_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def actualizarPais(self,pais_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.countries SET country_name = '{pais_param.country_name}', region_id = {pais_param.region_id} WHERE country_id = '{pais_param.country_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()

        except Exception as e:
            print(f"Error en la actualizacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarPais(self, country_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.countries WHERE country_id = '{country_param.country_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la eliminacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def buscarPais(self, country_param):
        listaPaises = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"SELECT c.country_id, c.country_name, r.region_name from Seguridad.countries as c " \
                  f"inner join Seguridad.regions as r on c.region_id = r.region_id " \
                  f"where c.country_name like '%{country_param.country_name}%';"

            #sql = f"SELECT c.country_id, c.country_name, r.region_name FROM Seguridad.countries AS c " \
             #     f"INNER JOIN Seguridad.regions AS r ON c.region_id = r.region_id " \
              #    f"WHERE c.country_name LIKE '%{country_param.country_name}%';"

            if not cursor.execute(sql) > 0:
                return

            registros = cursor.fetchall()
            for r in registros:
                id = r['country_id']
                nombre = r['country_name']
                region_name = r['region_name'] #No me gusta. Estamos creando un objeto Country con un atributo que no le corresponde
                pais = Country(id, nombre, region_name)
                listaPaises.append(pais)

        except Exception as e:
            print(f"Error en la busqueda: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaPaises


