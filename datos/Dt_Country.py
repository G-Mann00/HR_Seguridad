from datos.conexion import Conexion
from entidades.Country import Country
from entidades.VwCountries import VwCountries



class Dt_Country:
    _con = None
    _cursor = None

    def __init__(self):
        pass

    def listarPaises(self):
        listaPaises = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql ="SELECT * From Seguridad.VwCountries;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['country_id']
                nombre = r['country_name']
                region_name = r['region_name']
                vista = VwCountries(id, nombre, region_name)
                listaPaises.append(vista)
            return listaPaises
        except Exception as e:
            print("Datos: Error en listaPaises", e)
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

    def validarIdUnico(self, country_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT country_id FROM Seguridad.countries WHERE country_id = '{country_param.country_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def existePais(self, country_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT * FROM Seguridad.countries WHERE country_name = '{country_param.country_name}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
            return resultado
        except Exception as e:
            print("Datos: Error existePais()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()


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
            print(f"Datos: Error actualizarPais(): {e}")
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
            sql = f"SELECT * FROM Seguridad.VwCountries where country_name like '%{country_param.country_name}%';"

            resultados = cursor.execute(sql)
            print(f"Resultados: {resultados}")

            registros = cursor.fetchall()
            for r in registros:
                id = r['country_id']
                nombre = r['country_name']
                region_name = r['region_name'] #No me gusta. Estamos creando un objeto Country con un atributo que no le corresponde
                vista = VwCountries(id, nombre, region_name)
                listaPaises.append(vista)

        except Exception as e:
            print(f"Error en la busqueda: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaPaises


