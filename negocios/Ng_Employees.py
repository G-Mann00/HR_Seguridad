from datos.Dt_Employees import Dt_Employees
from entidades.Employees import Employees

class Ng_Employees:
    dEmployees = Dt_Employees()
    e = Employees()
    
    def __init__(self):
        pass
    
    # -1 = Error
    # 1 = Exito
    # 2 = Existe un registro con el mismo identificador
    # 3 = Existe un registro con el mismo correo
    def insertarEmpleado(self, employee_param):
        resultado = -1
        try:
            if self.dEmployees.validarIdUnico(employee_param):
                resultado = 2
                return resultado

            if self.dEmployees.existeCorreo(employee_param):
                resultado = 3
                return resultado

            if self.dEmployees.insertarEmpleado(employee_param):
                resultado = 1
            return resultado
        except Exception as e:
            print("Negocio: Error en insertarEmpleado()", e)
    
    def actualizarEmpleado(self, employee_param):
        resultado = False
        try:
            if self.dEmployees.actualizarEmpleado(employee_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en actualizarEmpleado()", e)
    
    def eliminarEmpleado(self, employee_param):
        resultado = False
        try:
            if self.dEmployees.eliminarEmpleado(employee_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en eliminarEmpleado()", e)
            
