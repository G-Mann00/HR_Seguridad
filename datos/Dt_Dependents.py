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
            print("Datos: Error en listarDependientes", e)

        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()

    def buscarDependiente(self, dependent_param):
        listaDependientes = []
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"SELECT * FROM Seguridad.VwDependents where first_name like '%{dependent_param.first_name}%';"

            resultados = cursor.execute(sql)
            print(f"Resultados: {resultados}")

            registros = self._cursor.fetchall()
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

