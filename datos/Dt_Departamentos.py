from datos.conexion import Conexion
from entidades.Departments import Departments
from entidades.Location import Location
from entidades.Vw_Location import Vw_Location

class Dt_Departamentos:

    def __init__(self):
        self._con = None
        self._cursor = None

    def listarDepartamentos(self):
        listaDepartamentos = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql ="SELECT d.department_id, d.department_name, l.city from Seguridad.departments as d inner join Seguridad.locations as l on d.location_id = l.location_id;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['department_id']
                nombre = r['department_name']
                city= r['city']
                departamento = Vw_Location(id, nombre, city)
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
            sql = f"INSERT INTO Seguridad.departments (department_id, department_name, location_id) " \
                  f"VALUES ('{departamento_param.department_id}', '{departamento_param.department_name}', {departamento_param.location_id});"
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
            sql = f"UPDATE Seguridad.departments SET department_name = '{departamento_param.department_name}', location_id = {departamento_param.location_id} WHERE department_id = '{departamento_param.department_id}';"
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
            sql = f"DELETE FROM Seguridad.departments WHERE department_id = '{departamento_param.department_id}';"
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
        listaDepartamentos = []
        try:
            con = Conexion.getConnection()
            cursor = self._con.cursor()
            sql = f"SELECT d.department_id, d.department_name, l.location_id from Seguridad.departments as d" \
                  f"inner join Seguridad.locations as l on d.location_id = l.location_id " \
                  f"WHERE d.department_id like '%{departamento_param.department_id}%';"

            if not cursor.execute(sql) > 0:
                return

            registros = cursor.fetchall()
            for r in registros:
                id = r['department_id']
                nombre = r['department_name']
                location_name = r['location_name']
                departamento = Departments(id, nombre, location_name)
                listaDepartamentos.append(departamento)
        except Exception as e:
            print(f"Error en la consulta:, {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaDepartamentos

