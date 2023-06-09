from datos.Dt_Dependents import Dt_Dependents
from entidades.Dependents import Dependents


class Ng_Dependent:
    dDependent = Dt_Dependents()
    d = Dependents()

    def __init__(self):
        pass

    # -1 = Error
    # 1 = Exito
    # 2 = Existe un registro con el mismo identificador
    def insertarDependiente(self, dependent_param):
        resultado = -1
        try:
            if self.dDependent.validarIdUnico(dependent_param):
                resultado = 2
                return resultado

            if self.dDependent.insertarDependiente(dependent_param):
                resultado = 1
            return resultado
        except Exception as e:
            print("Negocio: Error en insertarDependiente()", e)

    def actualizarDependiente(self, dependent_param):
        resultado = False
        try:
            if self.dDependent.actualizarDependiente(dependent_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en actualizarDependiente()", e)

    def eliminarDependiente(self, dependent_param):
        resultado = False
        try:
            if self.dDependent.eliminarDependiente(dependent_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en eliminarDependiente()", e)
