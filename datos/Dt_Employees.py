from datos.conexion import Conexion
from entidades.VwEmployees import VwEmployees
from entidades.Employees import Employees

class Dt_Employees:
    
    def __init__(self):
        self._con = None
        self._cursor = None
        
    def listarEmpleados(self):
        listaEmpleados = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = "SELECT * FROM Seguridad.VwEmployees"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r["employee_id"]
                primerNombre = r["first_name"]
                ultimoNombre = r["last_name"]
                email = r["email"]
                telefono = r["phone_number"]
                contratacion = r["hire_date"]
                trabajo = r["job"]
                salario = r["salary"]
                manager = r["manager"]
                departamento = r["department"]
                vista = VwEmployees(id, primerNombre, ultimoNombre, email, telefono, contratacion, trabajo, salario, manager, departamento)
                listaEmpleados.append(vista)
            return listaEmpleados    
        except Exception as e:
            print("Datos: Error en listarEmpleados", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
        
    def listarManagers(self):
        listaManagers = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = "SELECT * FROM Seguridad.employees WHERE employee_id IN (SELECT DISTINCT manager_id FROM employees);"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r["employee_id"]
                primerNombre = r["first_name"]
                ultimoNombre = r["last_name"]
                email = r["email"]
                telefono = r["phone_number"]
                contratacion = r["hire_date"]
                trabajo = r["job_id"]
                salario = r["salary"]
                manager = r["manager_id"]
                departamento = r["department_id"]
                vista = Employees(id, primerNombre, ultimoNombre, email, telefono, contratacion, trabajo, salario, manager, departamento)
                listaManagers.append(vista)
            return listaManagers    
        except Exception as e:
            print("Datos: Error en listarEmpleados", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
    
    def insertarEmpleado(self, employee_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"INSERT INTO Seguridad.employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id) " \
                  f"VALUES ('{employee_param.first_name}', '{employee_param.last_name}', '{employee_param.email}', '{employee_param.phone_number}', '{employee_param.hire_date}', '{employee_param.job_id}', '{employee_param.salary}', '{employee_param.manager_id}', '{employee_param.department_id}');"
            if self._cursor.execute(sql) > 0:
                resultado = True
            self._con.commit()      
        except Exception as e:
            print("Datos: Error en insertarEmpleado", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
    
    def validarIdUnico(self, employee_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT employee_id FROM Seguridad.employees WHERE employee_id = '{employee_param.employee_id}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
        except Exception as e:
            print("Error en la consulta", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
    
    def existeCorreo(self, employee_param):
        resultado = False
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT * FROM Seguridad.employees WHERE email = '{employee_param.email}';"
            if self._cursor.execute(sql) > 0:
                resultado = True
            return resultado
        except Exception as e:
            print("Datos: Error existeCorreo()", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
    
    def actualizarEmpleado(self, employee_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"UPDATE Seguridad.employees SET first_name = '{employee_param.first_name}', last_name = '{employee_param.last_name}', email = '{employee_param.email}', phone_number = '{employee_param.phone_number}', hire_date = '{employee_param.hire_date}', job_id = '{employee_param.job_id}', salary = '{employee_param.salary}', manager_id = '{employee_param.manager_id}', department_id = '{employee_param.department_id}' WHERE employee_id = '{employee_param.employee_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()

        except Exception as e:
            print(f"Datos: Error actualizarEmpleado(): {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
    
    def eliminarEmpleado(self, employee_param):
        resultado = False
        try:
            con = Conexion.getConnection()
            cursor = Conexion.getCursor()
            sql = f"DELETE FROM Seguridad.employees WHERE employee_id = '{employee_param.employee_id}';"
            if cursor.execute(sql) > 0:
                resultado = True
            con.commit()
        except Exception as e:
            print(f"Error en la eliminacion: {e}")
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
            return resultado
    
    def buscarEmpleado(self, employee_param):
        listaEmpleados = []
        try:
            self._con = Conexion.getConnection()
            self._cursor = self._con.cursor()
            sql = f"SELECT * FROM Seguridad.VwEmployees where first_name like '%{employee_param.first_name}%'"
            self._cursor.execute(sql)
            registros = self._cursor.fetchall()
            for r in registros:
                id = r["employee_id"]
                primerNombre = r["first_name"]
                ultimoNombre = r["last_name"]
                email = r["email"]
                telefono = r["phone_number"]
                contratacion = r["hire_date"]
                trabajo = r["job"]
                salario = r["salary"]
                manager = r["manager"]
                departamento = r["department"]
                vista = VwEmployees(id, primerNombre, ultimoNombre, email, telefono, contratacion, trabajo, salario, manager, departamento)
                listaEmpleados.append(vista)
            return listaEmpleados    
        except Exception as e:
            print("Datos: Error en buscarEmpleados", e)
        finally:
            Conexion.closeCursor()
            Conexion.closeConnection()
        