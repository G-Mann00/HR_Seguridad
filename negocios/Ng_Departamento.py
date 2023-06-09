from datos.Dt_Departamentos import Dt_Departamentos
from entidades.Departments import Departments

class Ng_Departamentos:
    def __init__(self):
        self.departamento = Departments()
    dd = Dt_Departamentos()

    def validarNombre(self, departamento, dep_id = None):
        departamentos = self.dd.listarDepartamentos()
        if dep_id is None:
            for dep in departamentos:
                if dep.department_name == departamento._department_name:
                    return False
        else:
            for dep in departamentos:
                if not dep_id == departamento._department_id:
                    if dep.department_name == departamento._department_name:
                        return False
        return True

    def insertarDepartamento(self, departamento):
        if not self.validarNombre(departamento):
            return False
        self.dd.insertarDepartamento(departamento)

    def actualizarDepartamento(self, departamento):
        if not self.validarNombre(departamento):
            return False
        self.dd.actualizarDepartamento(departamento)