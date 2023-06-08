from datos.conexion import Conexion
from entidades.Dependents import Dependents
from entidades.VwDependents import VwDependents


class Dt_Dependents:
    _con = None
    _cursor = None

    def __init__(self):
        pass

    def listarDependientes(self):
        listaDependientes = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = "SELECT * FROM Seguridad.VwDependents;"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r['dependent_id']
                primerNombre = r['first_name']
                ultimoNombre = r['last_name']
                relacion = r['relationship']
                empleado = r['employee_name']
                vista = VwDependents(id, primerNombre, ultimoNombre, relacion, empleado)
                listaDependientes.append(vista)
            return listaDependientes

        except Exception as e:
            print("Datos: Error en listarDependientes()", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def insertarDependiente(self, dependent_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"INSERT INTO Seguridad.dependents (first_name, last_name, relationship, employee_id) " \
                  f"VALUES ('{dependent_param.first_name}', '{dependent_param.last_name}', '{dependent_param.relationship}', '{dependent_param.employee_id}');"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()

        except Exception as e:
            print("Datos: error en insertarDependiente()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def validarIdUnico(self, dependent_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT dependent_id FROM Seguridad.dependents WHERE dependent_id = '{dependent_param.dependent_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def actualizarDependiente(self, dependent_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.dependents SET first_name = '{dependent_param.first_name}', last_name = '{dependent_param.last_name}', relationship = '{dependent_param.relationship}', employee_id = '{dependent_param.employee_id}' WHERE dependent_id = '{dependent_param.dependent_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()

        except Exception as e:
            print(f"Datos: Error actualizarDependiente(): {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def eliminarDependiente(self, dependent_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.dependents WHERE dependent_id = '{dependent_param.dependent_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Datos: Error en eliminarDependiente() : {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado

    def buscarDependiente(self, dependent_param):
        listaDependientes = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"SELECT * FROM Seguridad.VwDependents where first_name like '%{dependent_param.first_name}%';"

            resultados = cursor.execute(sql)
            print(f"Resultados: {resultados}")

            registros = cursor.fetchall()
            for r in registros:
                id = r['dependent_id']
                primerNombre = r['first_name']
                ultimoNombre = r['last_name']
                relacion = r['relationship']
                empleado = r['employee_name']
                vista = VwDependents(id, primerNombre, ultimoNombre, relacion, empleado)
                listaDependientes.append(vista)

        except Exception as e:
            print(f"Error en la busqueda: {e}")

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return listaDependientes

