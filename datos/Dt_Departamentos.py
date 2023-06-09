from datos.conexion import Conexion
from entidades.Departments import Departments
from entidades.Location import Location
from entidades.VwDepartment import VwDepartment

class Dt_Departamentos:

    def __init__(self):
        self._con = None
        self._cursor = None

    def listarDepartamentos(self):
        listaDepartamentos = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql ="SELECT * FROM Seguridad.VwDepartmentC WHERE estado <> 3;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['department_id']
                nombre = r['department_name']
                city= r['city']
                departamento = VwDepartment(id, nombre, city)
                listaDepartamentos.append(departamento)
            return listaDepartamentos
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def insertarDepartamento(self, departamento_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"INSERT INTO Seguridad.departments (department_name, location_id) SELECT '{departamento_param.department_name}', locations.location_id " \
                  f"FROM Seguridad.locations WHERE locations.city= '{departamento_param.city}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def validarIdUnico(self, department_id):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT department_id FROM Seguridad.departments WHERE department_id = '{department_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def actualizarDepartamento(self, departamento_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.departments AS d INNER JOIN Seguridad.locations AS l ON d.location_id = l.location_id " \
                  f"SET d.department_name = '{departamento_param.department_name}', d.location_id = (SELECT location_id FROM Seguridad.locations " \
                  f"WHERE city = '{departamento_param.city}') WHERE d.department_id = {departamento_param.department_id};"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()

        except Exception as e:
            print(f"Error en la actualizacion:, {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarDepartamento(self, departamento_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.departments SET estado = '3' WHERE department_id = '{departamento_param.department_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()

        except Exception as e:
            print(f"Error en la eliminacion:, {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def buscarDepartamento(self, departamento_param):
        listaDepartaments = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f" SELECT * from Seguridad.VwDepartmentC where department_name like '%{departamento_param.department_name}%' and estado <> 3;"

            resultados = cursor.execute(sql)
            print(f"Resultados: {resultados}")

            registros = cursor.fetchall()
            for r in registros:
                id = r['department_id']
                nombre = r['department_name']
                city = r['city']
                vista = VwDepartment(id, nombre, city)
                listaDepartaments.append(vista)
        except Exception as e:
            print(f"Error en la busqueda: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaDepartaments

